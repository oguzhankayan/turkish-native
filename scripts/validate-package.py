#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import json

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "README.tr.md",
    ROOT / "AGENTS.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CODE_OF_CONDUCT.md",
    ROOT / "SECURITY.md",
    ROOT / "CHANGELOG.md",
    ROOT / "LICENSE",
    ROOT / "agents" / "openai.yaml",
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / "evals" / "cases",
    ROOT / "references" / "01-sentence-architecture.md",
    ROOT / "references" / "02-verb-and-lexical-fit.md",
    ROOT / "references" / "03-product-ui-localization.md",
    ROOT / "references" / "04-marketing-model-copy.md",
    ROOT / "references" / "05-register-fidelity.md",
    ROOT / "references" / "06-domain-page-integrity.md",
    ROOT / "evals" / "README.md",
    ROOT / "evals" / "cases" / "06-domain-page-integrity.yaml",
]
for path in required:
    if not path.exists():
        errors.append(f"missing: {path.relative_to(ROOT)}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8") if (ROOT / "SKILL.md").exists() else ""
readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
readme_tr = (ROOT / "README.tr.md").read_text(encoding="utf-8") if (ROOT / "README.tr.md").exists() else ""
changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") if (ROOT / "CHANGELOG.md").exists() else ""

reference_text = "\n".join(p.read_text(encoding="utf-8") for p in sorted((ROOT / "references").glob("*.md"))) if (ROOT / "references").exists() else ""
patterns = [int(n) for n in re.findall(r"^### (\d+)\.", reference_text, re.M)]
if patterns and patterns != list(range(1, max(patterns) + 1)):
    errors.append(f"pattern numbering has gaps: {patterns}")

if patterns:
    for doc_name, doc in [("README.md", readme), ("README.tr.md", readme_tr)]:
        if str(len(patterns)) not in doc:
            errors.append(f"{doc_name} does not mention current pattern count {len(patterns)}")

version_match = re.search(r'metadata:\s*\n\s*version: "([^"]+)"', skill)
if version_match:
    version = version_match.group(1)
    plugin_path = ROOT / ".claude-plugin" / "plugin.json"
    if plugin_path.exists():
        plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
        if plugin.get("version") != version:
            errors.append("plugin.json version does not match SKILL.md")
    if f"## {version} " not in changelog:
        errors.append("CHANGELOG.md does not include current version")
else:
    errors.append("could not read SKILL.md version")

eval_count = 0
coverage = set()
eval_dir = ROOT / "evals" / "cases"
if eval_dir.exists():
    if yaml is None:
        errors.append("PyYAML is required to validate evals/cases/*.yaml")
    else:
        all_cases = []
        for path in sorted(eval_dir.glob("*.yaml")):
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            all_cases.extend(data.get("cases") or [])
        eval_count = len(all_cases)
        ids = [case.get("id") for case in all_cases]
        if eval_count < 100:
            errors.append(f"evaluation set is too small: {eval_count} (minimum 100)")
        if len(ids) != len(set(ids)):
            errors.append("duplicate evaluation case IDs")
        valid_patterns = set(patterns)
        bad_patterns = sorted({case.get("pattern") for case in all_cases if case.get("pattern") not in valid_patterns})
        if bad_patterns:
            errors.append(f"evals reference unknown patterns: {bad_patterns}")
        coverage = {case.get("pattern") for case in all_cases if case.get("pattern") in valid_patterns}
        missing = sorted(valid_patterns - coverage)
        if missing:
            errors.append(f"patterns without eval coverage: {missing}")
        positive_controls = sum(1 for case in all_cases if case.get("expected") == case.get("input"))
        if positive_controls < 10:
            errors.append(f"too few positive controls: {positive_controls} (minimum 10)")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)

print(f"OK: {len(patterns)} patterns, {eval_count} eval cases, full pattern coverage, package files present")
