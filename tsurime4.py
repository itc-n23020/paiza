def calculate_paiza_points(p):
    points = p // 100  # ポイント付与額
    if p >= 1000:
        points += 10  # ボーナスポイント

    print(points)


p = int(input())
calculate_paiza_points(p)
