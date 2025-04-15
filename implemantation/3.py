n = input()
x = int(ord(n[0]))-96
y = int(n[1])
nlst = [(1, -2), (-1, -2), (1, 2), (-1, 2), (-2, 1), (-2, 1), (2, 1), (2, -1)]
cnt = 0
for i in nlst:
    # print(x+i[0], y+i[1])
    if x+i[0] > 0 and y+i[1] > 0:
        cnt += 1
print(cnt)


