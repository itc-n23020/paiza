def check_ametama(n, m):
    if m % n == 0:
        print("ok")
    else:
        print("ng")


n, m = map(int, input().split())
check_ametama(n, m)
