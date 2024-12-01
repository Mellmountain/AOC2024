input = list(open('Day01/input.txt').read().splitlines())
left = []
right = []
count = dict()
for line in input:
    p1, p2 = line.split('   ')
    left.append(int(p1))
    right.append(int(p2))
    if p2 in count:
        counts = count[p2]
        count[p2] = counts + 1
    else:
        count[p2] = 1

left.sort()
right.sort()

part1 = 0
part2 = 0

for i, loc in enumerate(left):
    part1 +=  abs(loc - right[i])
    if str(loc) in count:
        part2 += loc * count[str(loc)]

print(part1) 
print(part2) 