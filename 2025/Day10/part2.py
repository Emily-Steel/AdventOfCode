from ast import Set, Tuple
import re
import sys
from pathlib import Path
from tqdm import tqdm

SELF_PATH = Path(__file__).parent

def debug_print(msg: str):
    if "--debug" in sys.argv:
        print(msg)

def parse_goal(row: str):
    match = re.search(r'\{(.*?)\}', row)
    return [int(x) for x in match.group(1).split(',')]

def parse_buttons(row: str):
    groups = re.findall(r'\((.*?)\)', row)
    buttons = []
    for group in groups:
        joltage_increments = [int(c) for c in group.split(',')]
        buttons.append(joltage_increments)
    return buttons

def parse_row(row: str):
    return parse_goal(row), parse_buttons(row)

def joltage_str(joltage: set):  
    return repr(joltage)

def button_str(button):
    return ' '.join([str(b) for b in button])

def joltage_after_pressing_button(joltage, button):
    new_joltage = joltage.copy()
    for joltage_to_increase in button:
        new_joltage[joltage_to_increase] += 1
    return new_joltage

def any_joltage_exceeds_goal(joltage, goal):
    for i in range(len(goal)):
        if joltage[i] > goal[i]:
            return True
    return False

def reorder_goal_and_buttons(goal, buttons):
    # Reorder the goal joltage in asc order, remap buttons so they refer to the new indices.
    indexed_goal = list(enumerate(goal))
    indexed_goal.sort(key=lambda x: x[1])
    index_mapping = {old_index: new_index for new_index, (old_index, _) in enumerate(indexed_goal)}
    new_goal = [value for _, value in indexed_goal]
    new_buttons = []
    for button in buttons:
        new_button = [index_mapping[i] for i in button]
        new_buttons.append(new_button)
    return new_goal, new_buttons

def solve_machine(machine):
    goal_joltage, buttons = machine
    starting_joltage_state = [0] * len(goal_joltage)
    machine_str = f"[{joltage_str(goal_joltage)}] {[button_str(b) for b in buttons]}"
    debug_print(machine_str)
    
    joltage_states_to_visit = [(starting_joltage_state, buttons)]
    
    for step in range(1000):
        next_joltage_states_to_visit = []
        for joltage_state, allowed_buttons in joltage_states_to_visit:
            debug_print(f"Visiting {joltage_str(joltage_state)} [Step {step}]")
            next_buttons = []
            for button in allowed_buttons:
                # Compute the new light state and stick it on the queue.
                new_joltage = joltage_after_pressing_button(joltage_state, button)
                debug_print(f"Pressing button that increments {button_str(button)} on joltage state '{joltage_str(joltage_state)}' and got '{joltage_str(new_joltage)}'")
                if new_joltage == goal_joltage:
                    return step + 1
                if not any_joltage_exceeds_goal(new_joltage, goal_joltage):
                    next_joltage_states_to_visit.append((new_joltage, next_buttons))
                    next_buttons.append(button)
            debug_print(f"Added {len(next_joltage_states_to_visit)} new states to visit.")
        joltage_states_to_visit = next_joltage_states_to_visit
    debug_print("---")
    # Reorder the goal joltage in asc order, remap buttons so they refer to the new indices.
    # for each goal joltage identifity the buttons that affect it and for each of them calculate what the new joltages would be after pressing the button enough times to get to the goal joltage and check whether the problem is solvable from there.
   
    
def part2(input_data):
    machines = [parse_row(line) for line in input_data]
    total_min_steps = 0
    if "--debug" not in sys.argv:
        machines = tqdm(machines)
    for machine in machines:
        total_min_steps += solve_machine(machine)
    return total_min_steps

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = [line.strip() for line in f.readlines()]
    result = part2(day_input)
    debug_print(f"Part 2: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part2.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    
    main()
