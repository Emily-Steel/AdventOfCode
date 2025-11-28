with open("input.txt", "r") as rows:
    total_signal = 0
    cycle = 1
    special_cycles = [20, 60, 100, 140, 180, 220]
    pending_add = 0
    x = 1
    while cycle <= 220:
        if cycle in special_cycles:
            print(f"current x is {x}, cycle {cycle} so adding {cycle * x} to total")
            total_signal += cycle * x
        if pending_add == 0:
            row = rows.readline().strip().split()
            if row[0] == "addx":
                pending_add = int(row[1])
        else:
            x += pending_add
            pending_add = 0
        cycle += 1

    print(f"Total signal is: {total_signal}")
