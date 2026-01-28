#!/usr/bin/env python3
import argparse
import html
import re
from pathlib import Path

BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
TAG_RE = re.compile(r"<[^>]+>")
WHITESPACE_RE = re.compile(r"\s+")


def strip_html(text: str) -> str:
    text = BR_RE.sub("\n", text)
    text = text.replace("</p>", "\n").replace("</P>", "\n")
    text = TAG_RE.sub("", text)
    text = html.unescape(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text


def iter_lines(input_dir: Path, max_line_length: int, min_line_length: int):
    for path in sorted(input_dir.glob("book-*.php")):
        raw = path.read_text(encoding="utf-8")
        cleaned = strip_html(raw)
        for line in cleaned.split("\n"):
            line = WHITESPACE_RE.sub(" ", line).strip()
            if not line:
                continue
            if len(line) < min_line_length:
                continue
            if max_line_length > 0 and len(line) > max_line_length:
                continue
            yield line


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prepare Pan Tadeusz dataset for makemore."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("pan-tadeusz/books"),
        help="Directory with Pan Tadeusz HTML/PHP books.",
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        default=Path("data/pan_tadeusz.txt"),
        help="Output text file with one line per sample.",
    )
    parser.add_argument(
        "--max-line-length",
        type=int,
        default=200,
        help="Skip lines longer than this (0 disables).",
    )
    parser.add_argument(
        "--min-line-length",
        type=int,
        default=3,
        help="Skip lines shorter than this.",
    )
    args = parser.parse_args()

    if not args.input_dir.exists():
        raise SystemExit(f"Input directory not found: {args.input_dir}")

    lines = list(iter_lines(args.input_dir, args.max_line_length, args.min_line_length))
    if not lines:
        raise SystemExit("No lines extracted; check input directory or filters.")

    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    args.output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} lines to {args.output_file}")


if __name__ == "__main__":
    main()
