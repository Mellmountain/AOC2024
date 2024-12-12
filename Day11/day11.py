from functools import cache
input = [0, 89741, 316108, 7641, 756, 9, 7832357, 91]

@cache
def count_stones(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count_stones(1, steps - 1)
    str_stone = str(stone) 
    length = len(str_stone)
    if length % 2 == 0:
        return count_stones(int(str_stone[:length // 2]), steps - 1) + count_stones(int(str_stone[length // 2:]), steps - 1)
    return count_stones(stone * 2024, steps - 1)

print(sum(count_stones(stone, 25) for stone in input))
print(sum(count_stones(stone, 75) for stone in input))





        


