"""Refresh per-file sizes and SHA-256 hashes in skills/eu-ai-act/SOURCE.json.

Usage: python3 scripts/hash_sources.py
Run after scripts/convert.py or after editing a plugin-authored reference.
Document metadata in SOURCE.json is kept; add new source documents by hand.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "skills" / "eu-ai-act"
GENERATED = ("references/articles", "references/annexes", "references/recitals")
SUPPLEMENTS = (
    "references/catalog.md",
    "references/timeline.md",
    "references/builder-playbook.md",
)


def entry(path):
    data = path.read_bytes()
    return {
        "reference": path.relative_to(ROOT).as_posix(),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def main():
    source = ROOT / "SOURCE.json"
    data = json.loads(source.read_text())
    texts = [entry(p) for d in GENERATED for p in sorted((ROOT / d).glob("*.md"))]
    texts.append(entry(ROOT / "references/index.md"))
    data["texts"] = texts
    data["supplements"] = [entry(ROOT / s) for s in SUPPLEMENTS]
    data["generated_by"] = "scripts/convert.py <act.xhtml> skills/eu-ai-act/references [<amending.xhtml> ...]"
    source.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(f"{len(texts)} texts, {len(SUPPLEMENTS)} supplements")


if __name__ == "__main__":
    main()
