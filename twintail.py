c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())

performance1 = c1 / p1
performance2 = c2 / p2

if performance1 > performance2:
    print(1)
else:
    print(2)
