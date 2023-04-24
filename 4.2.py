from random import randint

def min_multy(a, b):
    global K
    global M
    if K[a][b] == None:
        if b - a == 1:
            K[a][b] = 0
        else:
            K[a][b] = 10000000
            for k in range(a + 1, b):
                K[a][b] = min(K[a][b], M[a] * M[k] * M[b] +  min_multy(a, k) + min_multy(k, b))
    return K[a][b]

N = 26
M = [randint(1, 10) for a in range(N)]
K = [[None for a in range(N)] for b in range(N)]

print(min_multy(0, N-1))
