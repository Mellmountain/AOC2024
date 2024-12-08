input = list(open('Day07/input.txt').read().splitlines())

def is_valid(target, numbers, p2):
    if len(numbers) == 1:
        return target == numbers[0]
    if is_valid(target, [numbers[0] + numbers[1]] + numbers[2:], p2):
        return True
    if is_valid(target, [numbers[0] * numbers[1]] + numbers[2:], p2):
        return True
    if p2 and is_valid(target, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:], p2):
        return True
    return False

results = []
numbers = []
for line in input:
    (res, nums) = line.split(':')
    results.append(res)
    numbers.append(nums.split(sep=None))

part1 = 0
part2 = 0
for i, target in enumerate(results):
    target = int(target)
    nums = [int(x) for x in numbers[i]]
    if is_valid(target, nums, False):
        part1 += target
    if is_valid(target, nums, True):
        part2 += target

print(part1)
print(part2)
