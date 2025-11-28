total_clashes = 0

with open("input.txt", "r") as rows:
    for row in rows.readlines():
        row = row.strip()
        pairs = row.split(",")
        pairs = [p.split("-") for p in pairs]
        a = pairs[0]
        b = pairs[1]
        if int(a[0]) > int(b[0]):
            a, b = (b, a)
        print(f"a: {a}, b: {b}")
        if int(a[1]) >= int(b[0]):
            print("clash")
            total_clashes += 1

print("Total clashes", total_clashes)
