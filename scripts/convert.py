"""Convert the official Publications Office XHTML of the AI Act and its
amendments into one Markdown file per Article, Annex, and Recital, with each
2026 amendment quoted inside the file it changes. Standard library only.

Usage:
  python3 scripts/convert.py <act.xhtml> skills/eu-ai-act/references [<amending.xhtml> ...]

Pass amending acts oldest first. Each must contain an Article titled
"Amendments to Regulation (EU) 2024/1689".

Fetch the inputs (EUR-Lex blocks scripted clients; Cellar does not):
  curl -sL -H "Accept: application/xhtml+xml" -H "Accept-Language: eng" \
    https://publications.europa.eu/resource/celex/32024R1689 > act.xhtml
  curl -sL -H "Accept: application/xhtml+xml" -H "Accept-Language: eng" \
    https://publications.europa.eu/resource/celex/32026R1744 > omnibus.xhtml

Legal wording is never rewritten or merged. Only layout changes: headings
become Markdown headings and enumerated points become nested list items.
Amending text is quoted as published, next to the 2024 text it amends.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "{http://www.w3.org/1999/xhtml}"
CHAPTERS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII"]


def text_of(el):
    raw = "".join(el.itertext()).replace(" ", " ")
    return re.sub(r"\s+", " ", raw).strip()


def render(el, out, depth=0):
    for child in el:
        tag = child.tag.replace(NS, "")
        c = child.get("class") or ""
        if tag == "p":
            t = text_of(child)
            if not t:
                continue
            if "oj-ti-section-1" in c:
                out.append(f"\n# {t}\n")
            elif "oj-ti-section-2" in c:
                out.append(f"\n## {t}\n")
            elif "oj-ti-art" in c:
                out.append(f"\n### {t}\n")
            elif "oj-sti-art" in c:
                out.append(f"**{t}**\n")
            elif "oj-doc-ti" in c:
                out.append(f"\n# {t}\n" if t.startswith("ANNEX") else f"## {t}\n")
            elif "oj-ti-grseq-1" in c:
                out.append(f"\n#### {t}\n")
            else:
                out.append("  " * depth + t + "\n")
        elif tag == "table":
            for body in child:
                if body.tag != NS + "tbody":
                    continue
                for tr in body:
                    tds = [td for td in tr if td.tag == NS + "td"]
                    if len(tds) == 2:
                        sub = []
                        render(tds[1], sub, depth + 1)
                        first, _, rest = "".join(sub).strip("\n").lstrip().partition("\n")
                        out.append("  " * depth + f"- {text_of(tds[0])} {first}\n")
                        if rest.strip():
                            out.append(rest.rstrip("\n") + "\n")
                    else:
                        for td in tds:
                            render(td, out, depth)
        elif tag in ("div", "td", "tbody"):
            render(child, out, depth)


def to_markdown(elements):
    out = []
    for el in elements:
        holder = ET.Element(NS + "div")
        holder.append(el)
        render(holder, out)
    return re.sub(r"\n{3,}", "\n\n", "".join(out)).strip() + "\n"


def load(path):
    raw = re.sub(r"<!DOCTYPE[^>]*>", "", Path(path).read_text(encoding="utf-8"))
    root = ET.fromstring(raw)
    return {el.get("id"): el for el in root.iter() if el.get("id")}


def article_key(num):
    """'4a' -> '004a', '50' -> '050'."""
    m = re.fullmatch(r"(\d+)([a-z]?)", num)
    return f"{int(m.group(1)):03d}{m.group(2)}"


def split_articles(chapter_md):
    """Yield (number, title, location, body) for each Article in a chapter."""
    chapter = section = None
    pending = None  # which heading the next '## ' line names
    current = None
    for line in chapter_md.splitlines():
        m = re.match(r"# (CHAPTER|SECTION) ([IVX\d]+)$", line)
        if m:
            if current:
                yield current
                current = None
            pending = m.group(1)
            if pending == "CHAPTER":
                chapter, section = f"Chapter {m.group(2)}", None
            else:
                section = f"Section {m.group(2)}"
            continue
        if line.startswith("## ") and pending and current is None:
            title = line[3:].strip()
            if pending == "CHAPTER":
                chapter += " " + re.sub(r"\bai\b", "AI", title.capitalize())
            else:
                section += f" {title}"
            pending = None
            continue
        m = re.match(r"### Article (\d+)$", line)
        if m:
            if current:
                yield current
            location = chapter + (f", {section}" if section else "")
            current = [m.group(1), None, location, []]
            continue
        if current is not None:
            if current[1] is None and line.startswith("**"):
                current[1] = line.strip("*`")
            else:
                current[3].append(line)
    if current:
        yield current


def amending_act(doc):
    """Return (label, short, article number) for an act amending 2024/1689."""
    full = " ".join(text_of(el) for el in doc.values() if el.get("class") == "oj-doc-ti")
    m = re.search(r"(REGULATION|DIRECTIVE) \(EU\) (\d{4}/\d+)", full)
    if not m:
        raise ValueError("cannot read the amending act's number")
    short = m.group(2)
    label = f"{m.group(1).capitalize()} (EU) {short}"
    for key, el in doc.items():
        if re.fullmatch(r"art_\d+", key) and "Amendments to Regulation (EU) 2024/1689" in text_of(el):
            return label, short, key[4:]
    raise ValueError(f"{label} has no Article amending Regulation (EU) 2024/1689")


def split_amendment_points(doc, article):
    """Return one Article of an amending act as a list of (point, markdown)."""
    md = to_markdown([doc[f"art_{article}"]])
    points, current = [], None
    for line in md.splitlines():
        m = re.match(r"- \((\d+)\) ", line)
        if m:
            current = [m.group(1), [line]]
            points.append(current)
        elif current is not None:
            current[1].append(line)
    return [(n, "\n".join(lines)) for n, lines in points]


def amendment_targets(text):
    """Map one amending point to the Articles or Annexes it changes.

    Returns (targets, inserted) where inserted maps a new Article or Annex
    key to the quoted text that creates it.
    """
    first = text.splitlines()[0]
    inserted = {}
    heads = list(re.finditer(r"^### ‘?Article (\d+[a-z])$", text, re.MULTILINE))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        inserted[("article", h.group(1))] = text[h.start():end].strip()
    m = re.search(r"‘Annex ([IVX]+)\b", text)
    if "following Annex is added" in first and m:
        inserted[("annex", m.group(1))] = text
    if inserted:
        return [], inserted
    m = re.search(r"\bArticle (\d+[a-z]?)", first)
    if m:
        return [("article", m.group(1))], {}
    m = re.search(r"\bAnnex ([IVX]+)\b", first)
    if m:
        return [("annex", m.group(1))], {}
    raise ValueError(f"cannot place amending point: {first}")


def amendment_block(act, point, text):
    label, short, article = act
    return (
        f"## Amended by {label}, Article {article}, point ({point})\n\n"
        "Check the application date in Article 113 as amended. Where this amending text "
        "replaces, inserts, or deletes wording, it controls over the 2024 text below and "
        "over any earlier amendment above it.\n\n" + text.strip() + "\n"
    )


def main(act_src, dest, *amending_srcs):
    dest = Path(dest)
    act = load(act_src)

    articles = {}  # key -> dict(title, location, body)
    for num in CHAPTERS:
        for n, title, location, body in split_articles(to_markdown([act[f"cpt_{num}"]])):
            articles[n] = {"title": title, "location": location, "body": "\n".join(body).strip()}
    annexes = {}
    for num in CHAPTERS:
        md = to_markdown([act[f"anx_{num}"]])
        title = re.search(r"^## (.+)$", md, re.MULTILINE).group(1)
        body = re.sub(r"^# ANNEX [IVX]+\n## .+\n", "", md).strip()
        annexes[num] = {"title": title, "body": body}

    notes = {}  # (kind, key) -> [(short, block)], oldest act first
    inserted = {}  # (kind, key) -> (act, point, quoted)
    for src in amending_srcs:  # pass amending acts oldest first
        doc = load(src)
        meta = amending_act(doc)
        for point, text in split_amendment_points(doc, meta[2]):
            targets, new = amendment_targets(text)
            for target in targets:
                notes.setdefault(target, []).append((meta[1], amendment_block(meta, point, text)))
            for target, quoted in new.items():
                inserted[target] = (meta, point, quoted)

    files = {}
    for n, a in articles.items():
        parts = [f"# Article {n}: {a['title']}\n\n{a['location']}. Regulation (EU) 2024/1689.\n"]
        parts += [block for _, block in notes.get(("article", n), [])]
        parts.append("## Text as published in 2024\n\n" + a["body"] + "\n")
        files[f"articles/{article_key(n)}.md"] = "\n".join(parts)
    for num, a in annexes.items():
        parts = [f"# Annex {num}: {a['title']}\n\nRegulation (EU) 2024/1689.\n"]
        parts += [block for _, block in notes.get(("annex", num), [])]
        parts.append("## Text as published in 2024\n\n" + a["body"] + "\n")
        files[f"annexes/{num.lower()}.md"] = "\n".join(parts)
    for (kind, key), ((label, short, article), point, quoted) in inserted.items():
        name = f"articles/{article_key(key)}.md" if kind == "article" else f"annexes/{key.lower()}.md"
        title = f"Article {key}" if kind == "article" else f"Annex {key}"
        parts = [
            f"# {title} (inserted by {label})\n\n"
            f"Inserted by {label}, Article {article}, point ({point}). "
            "Check the application date in Article 113 as amended.\n"
        ]
        parts += [block for _, block in notes.get((kind, key), [])]
        parts.append("## Text as inserted\n\n" + quoted.strip() + "\n")
        files[name] = "\n".join(parts)

    recitals = to_markdown([act["pbl_1"]])
    for m in re.finditer(r"^- \((\d+)\) (.*?)(?=^- \(\d+\) |\Z)", recitals, re.MULTILINE | re.DOTALL):
        files[f"recitals/{int(m.group(1)):03d}.md"] = (
            f"# Recital {m.group(1)}\n\nRegulation (EU) 2024/1689. Recitals are not binding.\n\n"
            + m.group(2).strip() + "\n"
        )

    files["index.md"] = build_index(articles, annexes, notes, inserted)
    for name, text in files.items():
        path = dest / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(re.sub(r"\n{3,}", "\n\n", text), encoding="utf-8")
    print(f"{len(files)} files")


def build_index(articles, annexes, notes, inserted):
    def mark(target):
        acts = sorted({short for short, _ in notes.get(target, [])})
        return f" (amended by {', '.join(acts)})" if acts else ""

    rows, location = [], None
    keys = sorted(list(articles) + [k for (kind, k) in inserted if kind == "article"], key=article_key)
    for n in keys:
        if n in articles:
            a = articles[n]
            if a["location"] != location:
                location = a["location"]
                rows.append(f"\n## {location}\n")
            rows.append(f"- [Article {n}](articles/{article_key(n)}.md): {a['title']}{mark(('article', n))}")
        else:
            short = inserted[("article", n)][0][1]
            rows.append(f"- [Article {n}](articles/{article_key(n)}.md): inserted by {short}{mark(('article', n))}")
    rows.append("\n## Annexes\n")
    for num, a in annexes.items():
        rows.append(f"- [Annex {num}](annexes/{num.lower()}.md): {a['title']}{mark(('annex', num))}")
    for kind, key in inserted:
        if kind == "annex":
            rows.append(f"- [Annex {key}](annexes/{key.lower()}.md): inserted by {inserted[(kind, key)][0][1]}")
    return (
        "# Article and Annex index\n\n"
        "Generated by `scripts/convert.py`. One file per Article or Annex. Amended files open "
        "with the amending text, oldest act first, then the 2024 text. "
        "Recitals: `recitals/NNN.md`, for example `recitals/012.md`.\n"
        + "\n".join(rows) + "\n"
    )


if __name__ == "__main__":
    main(*sys.argv[1:])
