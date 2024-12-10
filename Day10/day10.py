from collections import deque
input = list(open('Day10/input.txt').read().splitlines())

trailheads = []
map = []

def get_children(node, value):
    result = []
    x, y = node
    if x - 1 >= 0 and map[y][x - 1] != -1 and value - map[y][x - 1] == -1:
        result.append((x - 1, y))
    if x + 1 < X and map[y][x + 1] != -1 and value - map[y][x + 1] == -1:
        result.append((x + 1, y))
    if y - 1 >= 0 and map[y - 1][x] != -1 and value - map[y - 1][x] == -1:
        result.append((x, y - 1))
    if y + 1 < Y and map[y + 1][x] != -1 and value - map[y + 1][x] == -1:
        result.append((x, y + 1))
    return result

for y, line in enumerate(input):
    row = []
    for x, chr in enumerate(line):
        if chr == ".": #for tests only
            row.append(-1)
        else:
            if chr == "0": 
                trailheads.append((x, y))
            row.append(int(chr))
    map.append(row)

X = len(input[0])
Y = len(map)

def score(map, x, y):
    queue = deque([(x, y)])
    summits = set()
    trails = 0
    while queue:
        x, y = queue.popleft()
        for nx, ny in get_children((x, y), map[y][x]):
            if map[ny][nx] == 9:
                summits.add((nx, ny))
                trails += 1
            else:
                queue.append((nx, ny))
    return (len(summits), trails)

print(sum(score(map, x, y)[0] for x, y in trailheads))
print(sum(score(map, x, y)[1] for x, y in trailheads))
