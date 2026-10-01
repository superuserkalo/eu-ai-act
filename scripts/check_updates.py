"""Check whether the bundled AI Act text or the guidance watch list is stale.

Usage: python3 scripts/check_updates.py [--today YYYY-MM-DD]

Asks the Publications Office SPARQL endpoint for every act that amends,
corrects, implements, or proposes to amend a bundled document, and reports
any not listed in tracking.json. Corrections count only when an English
version exists. Also reports watch-list links that fail or are due for review.

Exit code 0: nothing to do. 1: a report was printed. 2: the check itself failed.
"""
import datetime as dt
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = "https://publications.europa.eu/webapi/rdf/sparql"
USER_AGENT = "eu-ai-act-skill-update-check"
RELATIONS = {
    "resource_legal_amends_resource_legal": "amends",
    "resource_legal_corrects_resource_legal": "corrects",
    "resource_legal_based_on_resource_legal": "is based on",
    "resource_legal_proposes_to_amend_resource_legal": "proposes to amend",
}
# Sector 3 is legislation; 5....PC is a Commission legislative proposal.
RELEVANT_CELEX = re.compile(r"^3\d{4}[A-Z]\d+|^5\d{4}PC\d+")

QUERY = """
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT DISTINCT ?target ?rel ?celex ?date ?title WHERE {
  VALUES ?target { %s }
  ?t cdm:resource_legal_id_celex ?target .
  ?act ?p ?t .
  VALUES ?p { %s }
  BIND(STRAFTER(STR(?p), "#") AS ?rel)
  ?act cdm:resource_legal_id_celex ?celex .
  OPTIONAL { ?act cdm:work_date_document ?date }
  ?e cdm:expression_belongs_to_work ?act ;
     cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> ;
     cdm:expression_title ?title .
}
"""


def sparql(targets):
    values = " ".join(f'"{c}"^^<http://www.w3.org/2001/XMLSchema#string>' for c in targets)
    preds = " ".join(f"cdm:{r}" for r in RELATIONS)
    url = ENDPOINT + "?" + urllib.parse.urlencode({"query": QUERY % (values, preds)})
    req = urllib.request.Request(
        url, headers={"Accept": "application/sparql-results+json", "User-Agent": USER_AGENT}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        rows = json.load(resp)["results"]["bindings"]
    return [{k: v["value"] for k, v in row.items()} for row in rows]


def new_acts(rows, tracking):
    known = set(tracking["bundled"]) | set(tracking["reviewed"])
    found = {}
    for row in rows:
        celex = row["celex"]
        if celex in known or not RELEVANT_CELEX.match(celex):
            continue
        entry = found.setdefault(celex, {"date": row.get("date", "?"), "title": row["title"], "links": set()})
        entry["links"].add(f"{RELATIONS[row['rel']]} {row['target']}")
    return found


def link_status(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status
    except urllib.error.HTTPError as err:
        return err.code
    except OSError as err:
        return str(err)


def stale_watch(tracking, today, status=link_status):
    limit = dt.timedelta(days=tracking["review_after_days"])
    problems = []
    for item in tracking["watch"]:
        reviewed = dt.date.fromisoformat(item["last_reviewed"])
        code = status(item["url"])
        if not (isinstance(code, int) and code < 400):
            problems.append((item, f"link check failed: {code}"))
        elif today - reviewed > limit:
            problems.append((item, f"last reviewed {item['last_reviewed']}"))
    return problems


def report(acts, watch):
    lines = []
    if acts:
        lines += ["## New acts related to the bundled text", ""]
        for celex, a in sorted(acts.items(), key=lambda kv: kv[1]["date"]):
            lines.append(
                f"- `{celex}` ({a['date']}, {'; '.join(sorted(a['links']))}): {a['title']}"
                f"  \n  https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{celex}"
            )
        lines += [
            "",
            "For an amending act or English correction: fetch it, rerun `scripts/convert.py`, "
            "update `timeline.md` and the playbook, then add it to `bundled` in `tracking.json`. "
            "Otherwise add it to `reviewed` with a one-line reason.",
            "",
        ]
    if watch:
        lines += ["## Guidance to review", ""]
        for item, reason in watch:
            lines.append(f"- [{item['name']}]({item['url']}): {reason}. {item['why']}.")
        lines += [
            "",
            "Check each page for new or changed guidance. Update the skill if it changes what "
            "builders must do, then set `last_reviewed` in `tracking.json`.",
        ]
    return "\n".join(lines)


def main(argv):
    today = dt.date.today()
    if "--today" in argv:
        today = dt.date.fromisoformat(argv[argv.index("--today") + 1])
    tracking = json.loads((ROOT / "tracking.json").read_text())
    try:
        rows = sparql(tracking["bundled"])
    except OSError as err:
        print(f"SPARQL query failed: {err}", file=sys.stderr)
        return 2
    text = report(new_acts(rows, tracking), stale_watch(tracking, today))
    if text:
        print(text)
        return 1
    print("Up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
