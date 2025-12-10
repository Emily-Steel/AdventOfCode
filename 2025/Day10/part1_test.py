from part1 import lights_after_pressing_button, lights_str

def test_lights_str():
    assert lights_str([0, 0, 0, 0]) == '....'
    assert lights_str([1, 1, 1, 1]) == '####'

def test_lights_after_pressing_button():
    lights = [0, 0, 0, 0]
    button = [1, 3]
    new_lights = lights_after_pressing_button(lights, button)
    assert new_lights == [0, 1, 0, 1]
    new_lights = lights_after_pressing_button(new_lights, button)
    assert new_lights == [0, 0, 0, 0]

def test_lights_after_pressing_button_all():
    lights = [0, 0, 0, 0]
    button = [0, 1, 2, 3]
    new_lights = lights_after_pressing_button(lights, button)
    assert new_lights == [1, 1, 1, 1]

def test_lights_after_flipping_third():
    lights = [0, 0, 0, 0]
    button = [2]
    new_lights = lights_after_pressing_button(lights, button)
    assert new_lights == [0, 0, 1, 0]
