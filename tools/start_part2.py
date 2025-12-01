#!/usr/bin/env python3
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def copy_part1_to_part2(day: int):
    """Copy part1.py to part2.py in the specified day directory."""
    year = os.getenv("AOC_YEAR")

    if not year:
        print("Error: AOC_YEAR not set in .env file")
        sys.exit(1)

    # Get the root directory (parent of tools/)
    root_dir = Path(__file__).parent.parent
    day_dir = root_dir / year / f"Day{day}"

    part1_file = day_dir / "part1.py"
    part2_file = day_dir / "part2.py"

    if not part1_file.exists():
        print(f"Error: {part1_file} does not exist!")
        sys.exit(1)

    # Copy part1.py to part2.py
    with open(part1_file, "r") as src, open(part2_file, "w") as dst:
        dst.write(src.read())

    print(f"Copied {part1_file} to {part2_file}")


if __name__ == "__main__":
    # Try to get day from CLI argument, otherwise check environment variable
    if len(sys.argv) == 2:
        day_str = sys.argv[1]
    else:
        day_str = os.getenv("AOC_DAY")
        if not day_str:
            print("Error: Day not provided via CLI argument or AOC_DAY environment variable")
            print("Usage: python start_part2.py <day_number>")
            print("   or: Set AOC_DAY in .env file")
            sys.exit(1)

    try:
        day = int(day_str)
        if day < 1 or day > 25:
            print("Day must be between 1 and 25")
            sys.exit(1)
        copy_part1_to_part2(day)
    except ValueError:
        print("Day must be a valid integer")
        sys.exit(1)
