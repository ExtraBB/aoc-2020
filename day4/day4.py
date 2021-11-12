import re

# Read input
file = open("input")
lines = file.read().split('\n\n')
lines = [line.replace('\n', ' ') for line in lines]
file.close()

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_passport(passport, validate):
    fields = passport.split()

    valid = 0
    for field in fields:
        key, value = field.split(":")
        if key in required_fields and not validate or validate_field(key, value):
            valid += 1
    
    return valid == len(required_fields)


def validate_field(key, value):
    if key == "byr" and string_is_digit_in_range(value, 1920, 2002):
        return  True
    if key == "iyr" and string_is_digit_in_range(value, 2010, 2020):
        return  True
    if key == "eyr" and string_is_digit_in_range(value, 2020, 2030):
        return  True
    if key == "hgt":
        if value.endswith("cm"):
            return len(value) == 5 and string_is_digit_in_range(value[0:3], 150, 193)
        elif value.endswith('in'):
            return len(value) == 4 and string_is_digit_in_range(value[0:2], 59, 76)
    if key == "hcl" and re.match("^#[0-9a-f]{6}$", value):
        return True
    if key == "ecl" and value in eye_colors:
        return True
    if key == "pid" and len(value) == 9 and value.isdigit():
        return True
    return False

def string_is_digit_in_range(value, min, max):
    if not value.isdigit():
        return False
    digit = int(value)
    return digit >= min and digit <= max

print("Part 1: " + str(sum(check_passport(passport, False) for passport in lines)))
print("Part 2: " + str(sum(check_passport(passport, True) for passport in lines)))