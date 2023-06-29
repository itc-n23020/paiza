def display_progress(s, t):
    progress = "-" * s
    progress = progress[: t - 1] + "+" + progress[t:]
    print(progress)


s = int(input())
t = int(input())

display_progress(s, t)
