n, m, k = map(int, input().split())
nlst = list(map(int, input().split()))
result = 0
count = 0

sorted_lst = sorted(nlst, reverse=True)

first = sorted_lst[0]
second = sorted_lst[1]

while count < m:
    if count + k <= m:
        result += first * k
        count += k

    else:
        result += first * (m - count)
        count += (m - count)

    if count < m:
        result += second
        count += 1

print(result)


