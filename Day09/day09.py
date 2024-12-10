input = list(open('Day09/input.txt').read())

disk = []
fid = 0

for i, chr in enumerate(input):
    val = int(chr)
    if i % 2 == 0:
        disk += [fid] * val
        fid += 1
    else:
        disk += [-1] * val

free = [i for i, x in enumerate(disk) if x == -1]

for i in free:
    while disk[-1] == -1:
        disk.pop()
    if len(disk) <= i:
        break
    disk[i] = disk.pop()


part1 = sum(i * x for i, x in enumerate(disk))

files = {}
free_blocks = []
fid = 0
pos = 0

for i, chr in enumerate(input):
    val = int(chr)
    if i % 2 == 0:
        files[fid] = (pos, val)
        fid += 1
    else:
        if val != 0:
            free_blocks.append((pos, val))
    pos += val

while fid > 0:
    fid -= 1
    pos, size = files[fid]
    for i, (start, length) in enumerate(free_blocks):
        if start >= pos:
            free_blocks = free_blocks[:i]
            break
        if size <= length:
            files[fid] = (start, size)
            if size == length:
                free_blocks.pop(i)
            else:
                free_blocks[i] = (start + size, length - size)
            break

part2 = 0
for id, (pos, size) in files.items():
    for x in range(pos, pos + size):
        part2 += id * x

print(part1)
print(part2)