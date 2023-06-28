# 入力の受け取りとカウント
votes = [input() for _ in range(5)]
yes_count = votes.count("yes")
no_count = votes.count("no")

# より多い票数の方を出力
if yes_count > no_count:
    print("yes")
else:
    print("no")
