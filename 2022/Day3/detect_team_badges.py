from string import ascii_lowercase, ascii_uppercase


def split_contents(backpack: str):
    halfway = int(len(backpack) / 2)
    return (set(backpack[0:halfway]), set(backpack[halfway:]))


def letter_to_score(letter: str):
    if letter.isupper():
        return ascii_uppercase.index(letter) + 26 + 1
    return ascii_lowercase.index(letter) + 1


total = 0
squad = []
with open("input.txt", "r") as backpacks:
    for backpack in backpacks.readlines():
        squad.append(set(backpack.strip()))
        if len(squad) == 3:
            common_item = squad[0].intersection(squad[1], squad[2])
            print(f"intersection of all 3: {common_item}")
            squad = []
            for letter in common_item:
                score = letter_to_score(letter)
                total += score

print(f"The sum of all priorities of badges is {total}")
