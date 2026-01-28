#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sample from a Pan Tadeusz makemore model."
    )
    parser.add_argument(
        "--input-file",
        type=Path,
        default=Path("data/pan_tadeusz.txt"),
        help="Prepared dataset file.",
    )
    parser.add_argument(
        "--work-dir",
        type=Path,
        default=Path("runs/pan_tadeusz"),
        help="Directory with trained model checkpoints.",
    )
    parser.add_argument(
        "--makemore-script",
        type=Path,
        default=Path("makemore/makemore.py"),
        help="Path to makemore script.",
    )
    parser.add_argument(
        "--device",
        type=str,
        default=None,
        help="Device to use (cpu, cuda, mps).",
    )
    args, extra_args = parser.parse_known_args()

    if not args.input_file.exists():
        raise SystemExit(
            f"Dataset not found at {args.input_file}. Run scripts/prepare_pan_tadeusz.py first."
        )
    if not args.makemore_script.exists():
        raise SystemExit(f"makemore script not found at {args.makemore_script}.")

    cmd = [
        sys.executable,
        str(args.makemore_script),
        "-i",
        str(args.input_file),
        "-o",
        str(args.work_dir),
        "--sample-only",
    ]

    if args.device:
        cmd.extend(["--device", args.device])

    cmd.extend(extra_args)
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
