#!/usr/bin/env python3
"""WCAG 2.1 contrast ratio checker.

Usage:
  python3 contrast_check.py '#1a1a1a' '#ffffff'          # single pair
  python3 contrast_check.py pairs.json                    # [{"fg":"#..","bg":"#..","label":".."}, ...]

Thresholds: 4.5:1 normal text (AA), 3:1 large text / UI components (AA).
"""
import json
import sys


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"invalid hex color: #{h}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rel_luminance(rgb):
    def channel(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg, bg):
    l1 = rel_luminance(hex_to_rgb(fg))
    l2 = rel_luminance(hex_to_rgb(bg))
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def report(fg, bg, label=""):
    ratio = contrast_ratio(fg, bg)
    normal = "PASS" if ratio >= 4.5 else "FAIL"
    large = "PASS" if ratio >= 3.0 else "FAIL"
    tag = f" [{label}]" if label else ""
    print(f"{fg} on {bg}{tag}: {ratio:.2f}:1  normal-text(4.5:1)={normal}  large-text/UI(3:1)={large}")
    return ratio >= 4.5


def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0].lstrip("#") and args[1].lstrip("#"):
        ok = report(args[0], args[1])
        sys.exit(0 if ok else 1)
    elif len(args) == 1:
        with open(args[0]) as f:
            pairs = json.load(f)
        failures = 0
        for p in pairs:
            if not report(p["fg"], p["bg"], p.get("label", "")):
                failures += 1
        print(f"\n{len(pairs) - failures}/{len(pairs)} pairs pass normal-text AA")
        sys.exit(1 if failures else 0)
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
