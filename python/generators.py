def gen(N):
    for i in range(N):
        yield i ** 2  # Позже возобновить выполнение здесь

for i in gen(5):
    print(i, end=' : ')