def count_occurrences(string, pattern):
    count = string.count(pattern)
    return count


S = input()
pattern = "cat"
count = count_occurrences(S, pattern)
print(count)
