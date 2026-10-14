#!/usr/bin/env python3
"""Validate the held-out benchmark corpus independently from regression evals."""

from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "evals" / "benchmark" / "cases.yaml"
REQUIRED_DIMENSIONS = {
    "fidelity",
    "native_turkish",
    "pattern_resolution",
    "register",
    "restraint",
}
GROUP_BY_REFERENCE = {
    "01-sentence-architecture.md": "sentence-architecture",
    "02-verb-and-lexical-fit.md": "verb-and-lexical-fit",
    "03-product-ui-localization.md": "product-ui-localization",
    "04-marketing-model-copy.md": "marketing-and-model-copy",
    "05-register-fidelity.md": "register-fidelity-final-checks",
    "06-domain-page-integrity.md": "domain-and-page-integrity",
}
REQUIRED_CASE_FIELDS = {
    "id",
    "pattern",
    "group",
    "input",
    "instruction",
    "case_type",
    "positive_control",
    "dimensions",
    "exact_invariants",
}


def error(message: str) -> None:
    errors.append(message)


errors = []

if yaml is None:
    error("PyYAML is required to validate evals/benchmark/cases.yaml")
elif not CORPUS.exists():
    error(f"missing: {CORPUS.relative_to(ROOT)}")
else:
    data = yaml.safe_load(CORPUS.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        error("benchmark file must contain a YAML mapping")
        data = {}

    if not isinstance(data.get("version"), str) or not data["version"].strip():
        error("benchmark version must be a non-empty string")
    if not isinstance(data.get("description"), str) or not data["description"].strip():
        error("benchmark description must be a non-empty string")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        error("benchmark cases must be a non-empty list")
        cases = []

    pattern_groups = {}
    for reference_name, group in GROUP_BY_REFERENCE.items():
        reference = ROOT / "references" / reference_name
        if not reference.exists():
            error(f"missing reference: references/{reference_name}")
            continue
        text = reference.read_text(encoding="utf-8")
        for number in re.findall(r"^### (\d+)\.", text, re.MULTILINE):
            pattern_groups[int(number)] = group

    ids = []
    inputs = []
    for index, case in enumerate(cases, start=1):
        label = f"case {index}"
        if not isinstance(case, dict):
            error(f"{label} must be a mapping")
            continue

        missing = sorted(REQUIRED_CASE_FIELDS - set(case))
        if missing:
            error(f"{label} is missing fields: {', '.join(missing)}")
            continue

        case_id = case["id"]
        if not isinstance(case_id, str) or not case_id.strip():
            error(f"{label}.id must be a non-empty string")
        else:
            ids.append(case_id)

        source = case["input"]
        for field in ("group", "input", "instruction"):
            if not isinstance(case[field], str) or not case[field].strip():
                error(f"{label}.{field} must be a non-empty string")
        if isinstance(source, str) and source.strip():
            inputs.append(source)

        pattern = case["pattern"]
        if not isinstance(pattern, int) or isinstance(pattern, bool):
            error(f"{label}.pattern must be an integer")
        elif pattern not in pattern_groups:
            error(f"{label}.pattern references unknown pattern {pattern}")
        elif case.get("group") != pattern_groups[pattern]:
            error(
                f"{label} uses pattern {pattern} with group {case.get('group')!r}; "
                f"expected {pattern_groups[pattern]!r}"
            )

        case_type = case["case_type"]
        if case_type not in {"correction", "adaptation", "preservation"}:
            error(f"{label}.case_type must be correction, adaptation, or preservation")
        if not isinstance(case["positive_control"], bool):
            error(f"{label}.positive_control must be boolean")
        elif case["positive_control"] != (case_type == "preservation"):
            error(f"{label}.positive_control must match case_type preservation")

        dimensions = case["dimensions"]
        if not isinstance(dimensions, dict):
            error(f"{label}.dimensions must be a mapping")
        else:
            if set(dimensions) != REQUIRED_DIMENSIONS:
                error(
                    f"{label}.dimensions must contain exactly: "
                    f"{', '.join(sorted(REQUIRED_DIMENSIONS))}"
                )
            for name, value in dimensions.items():
                if not isinstance(value, str) or not value.strip():
                    error(f"{label}.dimensions.{name} must be a non-empty string")

        invariants = case["exact_invariants"]
        if not isinstance(invariants, list) or not invariants:
            error(f"{label}.exact_invariants must be a non-empty list")
        elif any(not isinstance(value, str) or not value.strip() for value in invariants):
            error(f"{label}.exact_invariants must contain only non-empty strings")

    if len(ids) != len(set(ids)):
        error("duplicate benchmark case IDs")
    if len(inputs) != len(set(inputs)):
        error("duplicate benchmark inputs")

if errors:
    for message in errors:
        print(f"ERROR: {message}")
    sys.exit(1)

print(f"OK: {len(cases)} benchmark cases, valid pattern/group associations, schema, and scoring dimensions")
