#!/usr/bin/env python3
import argparse
import html
import re
import urllib.request
from pathlib import Path

BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
TAG_RE = re.compile(r"<[^>]+>")
DEFAULT_SOURCE_URL = "https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt"


def strip_html(text: str) -> str:
    text = BR_RE.sub("\n", text)
    text = text.replace("</p>", "\n").replace("</P>", "\n")
    text = TAG_RE.sub("", text)
    text = html.unescape(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text


def load_source_text(source_url: str | None, source_file: Path | None) -> str:
    if source_file is not None:
        if not source_file.exists():
            raise SystemExit(f"Source file not found: {source_file}")
        return source_file.read_text(encoding="utf-8")
    if source_url is None:
        raise SystemExit("Either --source-url or --source-file is required.")
    with urllib.request.urlopen(source_url) as response:
        data = response.read()
    return data.decode("utf-8", errors="replace")


def iter_lines(text: str, max_line_length: int, min_line_length: int):
    cleaned = strip_html(text)
    for line in cleaned.splitlines():
        if line == "":
            yield line
            continue
        if min_line_length > 0 and len(line) < min_line_length:
            continue
        if max_line_length > 0 and len(line) > max_line_length:
            continue
        yield line


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prepare Pan Tadeusz dataset for makemore."
    )
    parser.add_argument(
        "--source-url",
        type=str,
        default=DEFAULT_SOURCE_URL,
        help="URL with the Pan Tadeusz text source.",
    )
    parser.add_argument(
        "--source-file",
        type=Path,
        default=None,
        help="Optional local text file to use instead of downloading.",
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
        default=0,
        help="Skip lines longer than this (0 disables).",
    )
    parser.add_argument(
        "--min-line-length",
        type=int,
        default=0,
        help="Skip lines shorter than this (0 disables).",
    )
    args = parser.parse_args()

    text = load_source_text(args.source_url, args.source_file)
    lines = list(iter_lines(text, args.max_line_length, args.min_line_length))
    if not lines:
        raise SystemExit("No lines extracted; check source or filters.")

    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    args.output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} lines to {args.output_file}")


if __name__ == "__main__":
    main()
