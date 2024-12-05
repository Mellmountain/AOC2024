input = list(open('Day04/input.txt').read().splitlines())

WS = []
for line in input:
    row = []
    for chr in line:
        row.append(chr)
    WS.append(row)

part1 = 0
part2 = 0
R = len(WS)
C = len(WS[0])
for r in range(0, R):
    for c in range(0, C):
        if c + 3 < C and WS[r][c] == 'X' and WS[r][c + 1] == 'M' and WS[r][c + 2] == 'A' and WS[r][c + 3] == 'S':
            part1 += 1
        if c - 3 >= 0 and WS[r][c] == 'X' and WS[r][c - 1] == 'M' and WS[r][c - 2] == 'A' and WS[r][c - 3] == 'S':
            part1 += 1
        if r - 3 >= 0 and WS[r][c] == 'X' and WS[r - 1][c] == 'M' and WS[r - 2][c] == 'A' and WS[r - 3][c] == 'S':
            part1 += 1
        if r + 3 < R and WS[r][c] == 'X' and WS[r + 1][c] == 'M' and WS[r + 2][c] == 'A' and WS[r + 3][c] == 'S':
            part1 += 1
        if r + 3 < R and c + 3 < C and WS[r][c] == 'X' and WS[r + 1][c + 1] == 'M' and WS[r + 2][c + 2] == 'A' and WS[r + 3][c + 3] == 'S':
            part1 += 1
        if r - 3 >= 0 and c - 3 >= 0 and WS[r][c] == 'X' and WS[r - 1][c - 1] == 'M' and WS[r - 2][c - 2] == 'A' and WS[r - 3][c - 3] == 'S':
            part1 += 1
        if r + 3 < R and c - 3 >= 0 and WS[r][c] == 'X' and WS[r + 1][c - 1] == 'M' and WS[r + 2][c - 2] == 'A' and WS[r + 3][c - 3] == 'S':
            part1 += 1
        if r - 3 >= 0  and c + 3 < C and WS[r][c] == 'X' and WS[r - 1][c + 1] == 'M' and WS[r - 2][c + 2] == 'A' and WS[r - 3][c + 3] == 'S':
            part1 += 1
        
        # M.S
        # .A.
        # M.S
        # center, top-left, down-left, top-right, down-right
        if 0 <= r + 1 < R and 0 <= c + 1 < C  and 0 <= r - 1 < R and 0 <= c - 1 < C and WS[r][c] == 'A' and WS[r - 1][c - 1] == 'M' and WS[r + 1][c - 1] == 'M' and WS[r - 1][c + 1] == 'S' and WS[r + 1][c + 1] == 'S':
            part2 += 1
        if 0 <= r + 1 < R and 0 <= c + 1 < C  and 0 <= r - 1 < R and 0 <= c - 1 < C and WS[r][c] == 'A' and WS[r - 1][c - 1] == 'S' and WS[r + 1][c - 1] == 'M' and WS[r - 1][c + 1] == 'S' and WS[r + 1][c + 1] == 'M':
            part2 += 1
        if 0 <= r + 1 < R and 0 <= c + 1 < C  and 0 <= r - 1 < R and 0 <= c - 1 < C and WS[r][c] == 'A' and WS[r - 1][c - 1] == 'S' and WS[r + 1][c - 1] == 'S' and WS[r - 1][c + 1] == 'M' and WS[r + 1][c + 1] == 'M':
            part2 += 1
        if 0 <= r + 1 < R and 0 <= c + 1 < C  and 0 <= r - 1 < R and 0 <= c - 1 < C and WS[r][c] == 'A' and WS[r - 1][c - 1] == 'M' and WS[r + 1][c - 1] == 'S' and WS[r - 1][c + 1] == 'M' and WS[r + 1][c + 1] == 'S':
            part2 += 1

print(part1)
print(part2)