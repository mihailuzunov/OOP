n, m = [int(p) for p in input().split(' ')]

snake = input()

matrix = []

last_symbols = ""
for i in range(n):
    matrix.append([])
    count = 0
    while len(matrix[i]) != m:
        if last_symbols:
            for char in last_symbols:
                if i % 2 != 0:
                    matrix[i].insert(0, char)
                else:
                    matrix[i].append(char)
            last_symbols = ""
        if i % 2 != 0:
            matrix[i].insert(0, snake[count])
        else:
            matrix[i].append(snake[count])
        count += 1
        if len(matrix[i]) == m:
            last_symbols = snake[count:]

for item in matrix:
    print("".join(item))