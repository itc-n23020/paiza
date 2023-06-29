def join_words(words):
    result = "_".join(words)
    return result


n = int(input())
words = [input() for _ in range(n)]
output = join_words(words)
print(output)
