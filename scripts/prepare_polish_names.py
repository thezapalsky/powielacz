#!/usr/bin/env python3
import argparse
import random
from pathlib import Path


def load_names(path: Path) -> list[str]:
    if not path.exists():
        raise SystemExit(f"Missing input file: {path}")
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge Polish female and male names and shuffle into data/names.txt."
    )
    parser.add_argument(
        "--female-file",
        type=Path,
        default=Path("data/names/polish_female_firstnames.txt"),
        help="Path to female first names file.",
    )
    parser.add_argument(
        "--male-file",
        type=Path,
        default=Path("data/names/polish_male_firstnames.txt"),
        help="Path to male first names file.",
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        default=Path("data/names.txt"),
        help="Output file path.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=3407,
        help="Random seed for shuffling.",
    )
    args = parser.parse_args()

    names = load_names(args.female_file) + load_names(args.male_file)
    rng = random.Random(args.seed)
    rng.shuffle(names)

    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    args.output_file.write_text("\n".join(names) + "\n", encoding="utf-8")
    print(f"Wrote {len(names)} names to {args.output_file}")


if __name__ == "__main__":
    main()
