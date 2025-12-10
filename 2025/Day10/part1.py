from ast import List, Set, Tuple
import re
import sys
from pathlib import Path

SELF_PATH = Path(__file__).parent

def parse_row(row: str):
    goal_str, button_str = re.match(r'^\[(.*)\] (.*)$', row).groups()
    goal = [ 0 if c == '.' else 1 for c in goal_str ]
    groups = re.findall(r'\((.*?)\)', button_str)
    buttons = []
    for group in groups:
        lights_toggled = [int(c) for c in group.split(',')]
        buttons.append(lights_toggled)
    return goal, buttons

def lights_str(lights):  
    return ''.join(['.' if l == 0 else '#' for l in lights])

def button_str(button):
    return ' '.join([str(b) for b in button])

def lights_after_pressing_button(lights, button):
    new_lights = lights.copy()
    for light_to_toggle in button:
        new_lights[light_to_toggle] = 1 if new_lights[light_to_toggle] == 0 else 0
    return new_lights

def solve_machine(machine):
    goal_lights, buttons = machine
    starting_light_state = [0] * len(goal_lights)
    machine_str = f"[{lights_str(goal_lights)}] {[button_str(b) for b in buttons]}"
    print(machine_str)
    
    states_seen: Set[Tuple[int]] = set()
    light_states_to_visit = [starting_light_state]
    
    for step in range(1000):
        next_light_states_to_visit = []
        for light_state in light_states_to_visit:
            print(f"Visiting {lights_str(light_state)} [Step {step}]")
            for button in buttons:                
                # Compute the new light state and stick it on the queue.
                new_lights = lights_after_pressing_button(light_state, button)
                print(f"Pressing button that flips {button_str(button)} on light state '{lights_str(light_state)}' and got '{lights_str(new_lights)}'")
                if new_lights == goal_lights:
                    return step + 1
                if tuple(new_lights) not in states_seen:
                    states_seen.add(tuple(new_lights))
                    next_light_states_to_visit.append(new_lights)
            print(f"Added {len(next_light_states_to_visit)} new states to visit.")
        light_states_to_visit = next_light_states_to_visit

            
        # generate all reachable states by pressing all buttons. Check if goal state and exit early if so.
        # Increment round number.
        
    print("---")
   
    
def part1(input_data):
    machines = [parse_row(line) for line in input_data]
    # goal is array[int] buttons is array[array[int]]
    total_min_steps = 0
    for machine in machines:
        total_min_steps += solve_machine(machine)
        
    return total_min_steps

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = [line.strip() for line in f.readlines()]
    result = part1(day_input)
    print(f"Part 1: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part1.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    
    main()
