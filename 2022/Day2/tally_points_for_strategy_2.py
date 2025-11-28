def name_for_shape_points(shape_points: int):
    return ["Unknown", "Rock", "Paper", "Scissors"][shape_points]


def points_for_shape(shape: str):
    return {
        "A": 1,
        "B": 2,
        "C": 3,
    }[shape]


def which_shape_to_get_outcome(their_shape: str, outcome: str):
    if outcome == "Y":
        return their_shape
    if outcome == "X":
        return {
            "A": "C",
            "B": "A",
            "C": "B",
        }[their_shape]
    return {
        "A": "B",
        "B": "C",
        "C": "A",
    }[their_shape]


def my_score_for_round(their_shape, my_shape):
    their_points = points_for_shape(their_shape)
    my_points = points_for_shape(my_shape)
    my_score = my_points
    if their_points == my_points:
        my_score += 3
    if (their_points == 3 and my_points == 1) or my_points - their_points == 1:
        my_score += 6
    return my_score


def narrate_the_round(their_shape: str, my_shape: str, target_outcome: str, round_score: int):
    their_points = points_for_shape(their_shape)
    my_points = points_for_shape(my_shape)
    print(f"---- ROUND {round_number} ----")
    print(f" Them: {name_for_shape_points(their_points)} {their_shape}({their_points})")
    print(f" Me: {name_for_shape_points(my_points)} {my_shape}({my_points})")
    print("")
    print(f" Resulting score: {round_score}")


total_score = 0
round_number = 0
with open("./strategy_guide.txt", "r") as rows:
    for row in rows.readlines():
        row = row.strip()
        their_shape, desired_outcome = row.split()
        my_shape = which_shape_to_get_outcome(their_shape, desired_outcome)
        round_score = my_score_for_round(their_shape, my_shape)
        # narrate_the_round(their_shape, target_outcome, round_score)
        total_score += round_score

print("Total score if you use this strategy: ", total_score)
