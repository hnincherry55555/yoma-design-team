#!/usr/bin/env python3
"""Validate design token JSON against Yoma Fleet naming conventions.

Usage: python3 validate_tokens.py tokens.json
Checks: kebab-case, category/role/modifier structure, allowed categories,
no literal color names in semantic roles, no raw hex outside color category.
"""
import json
import re
import sys

ALLOWED_CATEGORIES = {"color", "space", "type", "radius", "elevation", "border", "motion"}
LITERAL_COLOR_NAMES = {"blue", "red", "green", "yellow", "orange", "purple", "pink", "gray", "grey", "black", "white"}
SEGMENT_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def flatten(obj, prefix=""):
    """Yield (path, value) for leaf tokens. Supports nested dicts and W3C-style {value: ...}."""
    if isinstance(obj, dict):
        if "value" in obj and not isinstance(obj["value"], dict):
            yield prefix, obj["value"]
        else:
            for k, v in obj.items():
                yield from flatten(v, f"{prefix}/{k}" if prefix else k)
    else:
        yield prefix, obj


def validate(path, value):
    errors = []
    segments = path.split("/")
    if len(segments) < 2:
        errors.append(f"{path}: needs at least category/role")
    category = segments[0]
    if category not in ALLOWED_CATEGORIES:
        errors.append(f"{path}: category '{category}' not in {sorted(ALLOWED_CATEGORIES)}")
    for seg in segments:
        if not SEGMENT_RE.match(seg):
            errors.append(f"{path}: segment '{seg}' is not kebab-case")
    # Semantic naming: role segment must not be a literal color name
    if category == "color" and len(segments) >= 2 and segments[1] in LITERAL_COLOR_NAMES:
        errors.append(f"{path}: role '{segments[1]}' is a literal color name; use semantic roles (action, surface, text, feedback...)")
    # Raw hex only allowed under color/
    if isinstance(value, str) and value.startswith("#") and category != "color":
        errors.append(f"{path}: raw hex value in non-color category")
    return errors


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    try:
        with open(sys.argv[1]) as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"FAIL: cannot read/parse JSON: {e}")
        sys.exit(1)

    all_errors = []
    count = 0
    for path, value in flatten(data):
        count += 1
        all_errors.extend(validate(path, value))

    if all_errors:
        print(f"FAIL: {len(all_errors)} issue(s) in {count} token(s):")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"PASS: {count} tokens valid")


if __name__ == "__main__":
    main()
