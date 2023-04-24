from random import randint
n = int(input("Введите размер массива: "))
arr = [randint(-100,100) for i in range(n)]
print('Массив:', arr)

max_len = 1
current_len = 1
start_index = 0
for i in range(1, n):
    if arr[i] > arr[i-1]:
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
            start_index = i - max_len
        current_len = 1

if current_len > max_len:
    max_len = current_len
    start_index = n - max_len

print("Наибольшая непрерывная возрастающая последовательность:")
for i in range(start_index, start_index+max_len):
    print(arr[i], end=" ")
