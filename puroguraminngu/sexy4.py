def calculate_steps(m, n):
    steps = m - n
    if steps > 0:
        print(steps)
    else:
        print(0)


m, n = map(int, input().split())
calculate_steps(m, n)
