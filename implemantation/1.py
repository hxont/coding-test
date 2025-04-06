n = int(input())
lrud = list(input())
x, y = 1, 1

for i in lrud:
    nx, ny = x, y
    if i == 'R':
        ny += 1
    elif i == 'L':
        ny -= 1
    elif i == 'U':
        nx -= 1
    elif i == 'D':
        nx += 1

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)


