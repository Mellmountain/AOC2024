input = list(open('Day06/input.txt').read().splitlines())

visited = set()
walls = set()
guard = (0,0)

for y, line in enumerate(input):
    X = len(line)
    for x, chr in enumerate(line):
        if chr == "#":
            walls.add((x, y))
        elif chr == "^":
            guard = (x, y)

Y = len(input)
direction = "north"
x, y = guard

while 0 <= x < X and 0 <= y < Y:
    if direction == "north":
        if (x, y - 1) in walls:
            direction = "east"
        else:
            y -= 1
    if direction == "east":
        if (x + 1, y) in walls:
            direction = "south"
        else:
            x += 1
    if direction == "south":
        if (x, y + 1) in walls:
            direction = "west"
        else:
            y += 1
    if direction == "west":
        if (x - 1, y) in walls:
            direction = "north"
        else:
            x -= 1
    if 0 <= x < X and 0 <= y < Y:
        visited.add((x, y))

print(len(visited))

loop_guard = 0
loop_count = 0
visited = set()
for wy in range(Y):
    for wx in range(X):
        if (wx, wy) not in walls:
            walls.add((wx, wy))    
        else:
            continue
        x, y = guard
        direction = "north"
        visited = set()
        loop_guard = 0
        while 0 <= x < X and 0 <= y < Y:
            if direction == "north":
                if (x, y - 1) in walls:
                    direction = "east"
                else:
                    y -= 1
            if direction == "east":
                if (x + 1, y) in walls:
                    direction = "south"
                else:
                    x += 1
            if direction == "south":
                if (x, y + 1) in walls:
                    direction = "west"
                else:
                    y += 1
            if direction == "west":
                if (x - 1, y) in walls:
                    direction = "north"
                else:
                    x -= 1
            
            if (x, y) in visited:
                loop_guard += 1
                if loop_guard >= len(visited):
                    loop_count += 1
                    #print(wx,wy)
                    break

            if 0 <= x < X and 0 <= y < Y:
                visited.add((x, y))
        walls.remove((wx, wy))
    
print(loop_count)
    