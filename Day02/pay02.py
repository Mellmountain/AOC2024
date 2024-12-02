def is_safe(lst):
    inc_or_dec = (lst == sorted(lst)) or (lst == sorted(lst, reverse=True))
    safe = True
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])
        if not 1 <= diff <= 3:
            safe = False
        
    return inc_or_dec and safe

input = list(open('Day02/input.txt').read().splitlines())

part1 = 0
part2 = 0
for line in input:
    lst =  [int(item) for item in line.split()]
    if is_safe(lst):
        part1 += 1

    for i in range(len(lst)):
        plst = lst[:i] + lst[i + 1:]
        if is_safe(plst):
            part2 += 1
            break

print(part1)
print(part2)

