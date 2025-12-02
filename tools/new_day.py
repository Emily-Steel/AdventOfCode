#!/usr/bin/env python3
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
import subprocess

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def update_env_file(env_path: Path, day: int):
    """Update the .env file to set AOC_DAY to the specified day."""
    if not env_path.exists():
        print(f"Warning: {env_path} does not exist")
        return

    # Read the current .env file
    with open(env_path, "r") as f:
        lines = f.readlines()

    # Update or add AOC_DAY
    day_found = False
    for i, line in enumerate(lines):
        if line.startswith("AOC_DAY="):
            lines[i] = f"AOC_DAY={day}\n"
            day_found = True
            break

    if not day_found:
        # Add AOC_DAY at the end
        if lines and not lines[-1].endswith("\n"):
            lines.append("\n")
        lines.append(f"AOC_DAY={day}\n")

    # Write back to the file
    with open(env_path, "w") as f:
        f.writelines(lines)

    print(f"Updated .env: AOC_DAY={day}")


def create_day_directory(day: int):
    """Create a new day directory structure for Advent of Code."""
    year = os.getenv("AOC_YEAR")

    if not year:
        print("Error: AOC_YEAR not set in .env file")
        sys.exit(1)

    # Get the root directory (parent of tools/)
    root_dir = Path(__file__).parent.parent
    template_dir = Path(__file__).parent / "day_template"
    day_dir = root_dir / year / f"Day{day}"

    if day_dir.exists():
        print(f"Directory {day_dir} already exists!")
        return

    # Create the directory
    day_dir.mkdir(parents=True, exist_ok=True)

    # Manually create input.txt (since it's gitignored)
    input_file = day_dir / "input.txt"
    input_file.touch()
    
    # Copy all files from template directory
    if template_dir.exists():
        for template_file in template_dir.iterdir():
            if template_file.is_file():
                dest_file = day_dir / template_file.name
                dest_file.write_text(template_file.read_text())
    else:
        print(f"Warning: Template directory {template_dir} does not exist")

    print(f"Created directory: {day_dir}")
    # Print directory structure
    try:
        result = subprocess.run(
            ["tree", "-L", "1", str(day_dir)],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print(result.stdout)
        else:
            raise FileNotFoundError
    except (FileNotFoundError, subprocess.TimeoutExpired):
        # Fallback to ls or manual listing
        print(f"\nCreated files in {day_dir.name}:")
        for file in sorted(day_dir.iterdir()):
            print(f"  {file.name}")

    # Update the .env file with the new day
    env_path = Path(__file__).parent.parent / ".env"
    update_env_file(env_path, day)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: python new_day.py [<day_number>]")
        sys.exit(1)

    try:
        if len(sys.argv) == 1:
            day_str = os.getenv("AOC_DAY")
            if not day_str:
                print("Error: Day not provided via CLI argument or AOC_DAY environment variable")
                print("Usage: python new_day.py <day_number>")
                print("   or: Set AOC_DAY in .env file to get it automatically incremented")
                sys.exit(1)
            day = int(day_str) + 1
        else:
            day = int(sys.argv[1])
        if day < 1 or day > 25:
            print("Day must be between 1 and 25")
            sys.exit(1)
        create_day_directory(day)
    except ValueError:
        print("Day must be a valid integer")
        sys.exit(1)
