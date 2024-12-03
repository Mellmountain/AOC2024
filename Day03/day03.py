import re
input = list(open('Day03/input.txt').read().splitlines())

part1 = 0
part2 = 0
skip = False
for line in input:
    matches = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
    for match in matches:
        num1, num2 = match
        part1 += int(num1) * int(num2)

    matches = re.finditer("mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don[']t\(\)", line)
    for match in matches:
        expr = match.group(0)
        print(expr, skip)
        if expr.startswith("mul") and not skip:
            num1, num2 = match.group(1), match.group(2)
            part2 += int(num1) * int(num2)
        elif expr ==  "do()":
            skip = False
        elif expr == "don't()":
            skip = True
            
print(part1)
print(part2)