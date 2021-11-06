file = open("input")
lines = file.readlines()
pattern_len = len(lines[0])


def part1(lines, right, down):
    count = 0
    pattern_len = len(lines[0])
    x = 0
    y = 0
    while y < len(lines) - down:
        x += right
        y += down
        if lines[y][x % (pattern_len - 1)] == "#":
            count += 1
    return count


def part2(lines):
    return part1(lines, 1, 1) * part1(lines, 3, 1) * part1(lines, 5, 1) * part1(lines, 7, 1) * part1(lines, 1, 2)


print("Part 1: " + str(part1(lines, 3, 1)))
print("Part 2: " + str(part2(lines)))
