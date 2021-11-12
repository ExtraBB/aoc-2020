file = open("input")
lines = file.readlines()

def parse_line(line):
    split = line.split(":")
    split2 = split[0].split()
    split3 = split2[0].split("-")
    return (split[1].strip(), split2[1], int(split3[0]), int(split3[1]))

def part1(lines):
    correct = 0
    for line in lines:
        (password, char, min, max) = parse_line(line)
        numChars = password.count(char)
        if numChars >= min and numChars <= max:
            correct += 1
    return correct

def part2(lines):
    correct = 0
    for line in lines:
        (password, char, pos1, pos2) = parse_line(line)
        if password[pos1 - 1] == char and password[pos2 - 1] != char or password[pos1 - 1] != char and password[pos2 - 1] == char:
            correct += 1
    return correct

print("Part 1: " + str(part1(lines)))
print("Part 2: " + str(part2(lines)))