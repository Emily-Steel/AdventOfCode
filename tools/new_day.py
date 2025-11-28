#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

def update_env_file(env_path: Path, day: int):
    """Update the .env file to set AOC_DAY to the specified day."""
    if not env_path.exists():
        print(f"Warning: {env_path} does not exist")
        return
    
    # Read the current .env file
    with open(env_path, 'r') as f:
        lines = f.readlines()
    
    # Update or add AOC_DAY
    day_found = False
    for i, line in enumerate(lines):
        if line.startswith('AOC_DAY='):
            lines[i] = f'AOC_DAY={day}\n'
            day_found = True
            break
    
    if not day_found:
        # Add AOC_DAY at the end
        if lines and not lines[-1].endswith('\n'):
            lines.append('\n')
        lines.append(f'AOC_DAY={day}\n')
    
    # Write back to the file
    with open(env_path, 'w') as f:
        f.writelines(lines)
    
    print(f"Updated .env: AOC_DAY={day}")

def create_day_directory(day: int):
    """Create a new day directory structure for Advent of Code."""
    year = os.getenv('AOC_YEAR')
    
    if not year:
        print("Error: AOC_YEAR not set in .env file")
        sys.exit(1)
    
    # Get the root directory (parent of tools/)
    root_dir = Path(__file__).parent.parent
    day_dir = root_dir / year / f"Day{day}"
    
    if day_dir.exists():
        print(f"Directory {day_dir} already exists!")
        return
    
    # Create the directory
    day_dir.mkdir(parents=True, exist_ok=True)
    
    # Create an empty input.txt file
    for filename in ["example.txt", "input.txt", "part1.py", "part1_test.py"]:
        file_path = day_dir / filename
        file_path.touch()
    
    print(f"Created directory: {day_dir}")
    print(f"Created files: example.txt, input.txt, part1.py, part1_test.py")
    
    # Update the .env file with the new day
    env_path = Path(__file__).parent.parent / '.env'
    update_env_file(env_path, day)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python new_day.py <day_number>")
        sys.exit(1)
    
    try:
        day = int(sys.argv[1])
        if day < 1 or day > 25:
            print("Day must be between 1 and 25")
            sys.exit(1)
        create_day_directory(day)
    except ValueError:
        print("Day must be a valid integer")
        sys.exit(1)
