from collections import deque


def get_index():
    with open("input.txt", "r") as data:
        message = data.read()
        window = deque()
        for i, c in enumerate(message):
            if len(window) < 13:
                window.append(c)
                continue
            if len(window) == 13:
                window.append(c)
                if len(set(window)) == len(window):
                    return i
                continue
            window.popleft()
            window.append(c)
            print(f"window: {window}")
            if len(set(window)) == len(window):
                return i
    return -1


print(get_index())
