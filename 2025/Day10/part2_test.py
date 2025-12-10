from part2 import joltage_str, joltage_after_pressing_button, parse_goal

def test_joltage_str():
    assert joltage_str([3, 5, 4, 7]) == '[3, 5, 4, 7]'

def test_parse_goal():
    input_row = '[3,5,4,7] (0,1) (2,3) {1,2}'
    goal = parse_goal(input_row)
    assert goal == [1, 2]

def test_reorder_goal_and_buttons():
    from part2 import reorder_goal_and_buttons
    goal = [5, 3, 7, 4]
    buttons = [[0, 2], [1, 3]]
    new_goal, new_buttons = reorder_goal_and_buttons(goal, buttons)
    assert new_goal == [3, 4, 5, 7]
    assert new_buttons == [[2, 3], [0, 1]]

def test_reorder_goal_and_buttons():
    from part2 import reorder_goal_and_buttons
    goal = [5, 3, 7, 4]
    buttons = [[2, 0], [1, 3]]
    new_goal, new_buttons = reorder_goal_and_buttons(goal, buttons)
    assert new_goal == [3, 4, 5, 7]
    assert new_buttons == [[3, 2], [0, 1]]


def test_joltage_after_pressing_button():
    joltage = [0, 0, 0, 0]
    button = [1, 3]
    new_joltage = joltage_after_pressing_button(joltage, button)
    assert new_joltage == [0, 1, 0, 1]
    new_joltage = joltage_after_pressing_button(new_joltage, button)
    assert new_joltage == [0, 2, 0, 2]

def test_joltage_after_pressing_button_all():
    joltage = [0, 0, 0, 0]
    button = [0, 1, 2, 3]
    new_joltage = joltage_after_pressing_button(joltage, button)
    assert new_joltage == [1, 1, 1, 1]

def test_joltage_after_flipping_third():
    joltage = [0, 0, 0, 0]
    button = [2]
    new_joltage = joltage_after_pressing_button(joltage, button)
    assert new_joltage == [0, 0, 1, 0]
    button = [0, 1, 2, 3]
    new_joltage = joltage_after_pressing_button(new_joltage, button)
    assert new_joltage == [1, 1, 2, 1]