file = open("input")
lines = file.readlines()
nums = list(map(lambda line: int(line), lines))

def part1(nums, target):
    rests = set()

    for x in nums:
        rest = target - x
        if rest in rests:
            return rest * x
        rests.add(x)


def part2(nums, target):
    for x in nums:
        found = part1(nums, target - x)
        if found:
            return found * x

print("Part 1: " + str(part1(nums, 2020)))
print("Part 2: " + str(part2(nums, 2020)))
