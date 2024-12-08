input = list(open('Day08/input.txt').read().splitlines())

antennas = {}
antinodes = set()
antinodes_p2 = set()

Y = len(input)
X = len(input[0])

for y, line in enumerate(input):
    for x, chr in enumerate(line):
        if chr != ".":
            if chr in antennas.keys():
                coords = antennas[chr]
                coords.append((x, y))
                antennas[chr] = coords
            else:
                coords = []
                coords.append((x, y))
                antennas[chr] = coords

for key in antennas.keys():
    coords = antennas[key]
    for coord1 in coords:
        for coord2 in coords:
            if coord1 == coord2:
                continue
            x1, y1 = coord1
            x2, y2 = coord2

            xn = x1 + (x1 - x2)
            yn = y1 + (y1 - y2)
            
            if 0 <= xn < X and 0 <= yn < Y:
                antinodes.add((xn,yn))
                while 0 <= xn < X and 0 <= yn < Y:
                    antinodes_p2.add((xn, yn)) 
                    xn += (x1 - x2)
                    yn += (y1 - y2)

for key in antennas.keys():
    if len(antennas[key]) <= 1:
        continue
    else:
        for coord in antennas[key]:
            antinodes_p2.add(coord)

print(len(antinodes))
print(len(antinodes_p2))

