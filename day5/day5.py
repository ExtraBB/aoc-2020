# Read input
file = open("input")
lines = file.read().splitlines()

def find_row(line):
    min = 0
    max = 127
    for char in line[0:7]:
        if char == 'F':
            max = max - (max - min + 1) / 2
        elif char == 'B':
            min = min + (max - min + 1) / 2
    return max

def find_seat(line):
    min = 0
    max = 7
    for char in line[7:11]:
        if char == 'L':
            max = max - (max - min + 1) / 2
        elif char == 'R':
            min = min + (max - min + 1) / 2
    return max

def find_highest_seat_id(lines):
    return max(find_row(line) * 8 + find_seat(line) for line in lines)

def find_open_seat(lines):
    seats = sorted([find_row(line) * 8 + find_seat(line) for line in lines])
    for i, seat in enumerate(seats):
        if i + 1 < len(seats) and seats[i + 1] - seat == 2:
            return seat + 1
    return 0

print("Part 1: " + str(find_highest_seat_id(lines)))
print("Part 2: " + str(find_open_seat(lines)))