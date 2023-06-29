def check_movie_availability(s, n):
    if s >= n:
        print("OK")
    else:
        print("NG")


s, n = map(int, input().split())

check_movie_availability(s, n)
