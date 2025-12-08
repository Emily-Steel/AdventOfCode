#!/usr/bin/env python3
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
import subprocess

# Load environment variables from .env file
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)


def find_latest_part(year: int, day: int) -> str:
    """Find the latest existing part file for the given day."""
    day_dir = Path(__file__).resolve().parent / str(year) / f"Day{day}"
    
    if not day_dir.exists():
        print(f"Error: Directory {day_dir} does not exist!")
        sys.exit(1)
    
    # Check for part2.py first, then part1.py
    for part in [2, 1]:
        part_file = day_dir / f"part{part}.py"
        if part_file.exists():
            return f"part{part}.py"
    
    print(f"Error: No part files found in {day_dir}")
    sys.exit(1)


def run_solution(year: int, day: int, part: str = None, use_example: bool = False):
    """Run the specified solution."""
    day_dir = Path(__file__).resolve().parent / str(year) / f"Day{day}"
    
    if part:
        part_file = day_dir / f"part{part}.py"
        if not part_file.exists():
            print(f"Error: {part_file} does not exist!")
            sys.exit(1)
        script_to_run = f"part{part}.py"
    else:
        script_to_run = find_latest_part(year, day)
    
    # Build the command
    cmd = ["uv", "run", f"{year}/Day{day}/{script_to_run}"]
    
    # Add -e flag if using example
    if use_example:
        cmd.append("-e")
    
    print(f"Running: {' '.join(cmd)}")
    
    # Run the command
    try:
        result = subprocess.run(cmd, cwd=Path(__file__).resolve().parent)
        sys.exit(result.returncode)
    except FileNotFoundError:
        print("Error: 'uv' command not found. Make sure uv is installed and in your PATH.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(1)


if __name__ == "__main__":
    # Parse command line arguments
    use_example = False
    part_arg = None
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "-e":
            use_example = True
        elif arg.isdigit() and part_arg is None:
            part_arg = arg
        else:
            print(f"Unknown argument: {arg}")
            print("Usage: python run_solution.py [-e] [part_number]")
            print("  -e: Use example input")
            print("  part_number: Specify which part to run (1 or 2)")
            sys.exit(1)
        i += 1
    
    # Get year and day from environment variables
    year_str = os.getenv("AOC_YEAR")
    day_str = os.getenv("AOC_DAY")
    
    if not year_str:
        print("Error: AOC_YEAR not set in .env file")
        sys.exit(1)
    
    if not day_str:
        print("Error: AOC_DAY not set in .env file")
        sys.exit(1)
    
    try:
        year = int(year_str)
        day = int(day_str)
        
        if part_arg:
            part = int(part_arg)
            if part not in [1, 2]:
                print("Error: Part must be 1 or 2")
                sys.exit(1)
            run_solution(year, day, str(part), use_example)
        else:
            run_solution(year, day, None, use_example)
            
    except ValueError:
        print("Error: AOC_YEAR and AOC_DAY must be valid integers")
        sys.exit(1)