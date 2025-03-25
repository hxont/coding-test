n, m = map(int, input().split())
nlst = []

for _ in range(n):
    num = list(map(int, input().split()))
    nlst.append(num)

min_num = [min(num) for num in nlst]

print(max(min_num))
