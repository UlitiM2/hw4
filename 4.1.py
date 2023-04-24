N = int(input("Введите количество экспонатов: "))
M = int(input("Введите количество заходов: "))
K = int(input("Введите вместимость рюкзака: "))

w = [0] * (N+1)
c = [0] * (N+1)

for i in range(1, N+1):
    w[i] = int(input(f"Введите вес {i}-го экспоната: "))
    c[i] = int(input(f"Введите ценность {i}-го экспоната: "))

dp = [[0] * (M+1) for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + c[i])
        else:
            dp[i][j] = dp[i-1][j]

print("Максимальная сумма ценности, которую можно унести:", dp[N][M])

items = []
j = M

for i in range(N, 0, -1):
    if dp[i][j] != dp[i-1][j]:
        items.append(i)
        j -= w[i]

print("Украденные экспонаты:", items[::-1])
