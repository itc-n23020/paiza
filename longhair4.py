def check_luckiness(N):
    if N % 7 == 0:
        print("lucky")
    else:
        print("unlucky")


N = int(input())
check_luckiness(N)
