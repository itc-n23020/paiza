def check_direction():
    correct_count = 0

    for _ in range(5):
        d, e = input().split()

        if d == e:
            correct_count += 1

    if correct_count >= 3:
        print("OK")
    else:
        print("NG")


check_direction()
