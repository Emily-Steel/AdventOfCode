from string import ascii_lowercase, ascii_uppercase


def split_contents(backpack: str):
    halfway = int(len(backpack) / 2)
    return (set(backpack[0:halfway]), set(backpack[halfway:]))


def letter_to_score(letter: str):
    if letter.isupper():
        return ascii_uppercase.index(letter) + 26 + 1
    return ascii_lowercase.index(letter) + 1


total = 0
with open("input.txt", "r") as backpacks:
    for backpack in backpacks.readlines():
        left, right = split_contents(backpack.strip())
        duplicate = left.intersection(right)
        for letter in duplicate:
            score = letter_to_score(letter)
            print(f"left: {left}, right: {right}, duplicated: {letter}, scored at {score}")
            total += score

print(f"The sum of all priorities of duplicate items is {total}")
