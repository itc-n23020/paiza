def compare_performance(c1, p1, c2, p2):
    performance1 = c1 / p1
    performance2 = c2 / p2

    if performance1 > performance2:
        return 1
    else:
        return 2


c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())

result = compare_performance(c1, p1, c2, p2)
print(result)
