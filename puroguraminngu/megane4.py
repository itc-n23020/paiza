def find_middle_number(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    middle_index = (len(numbers) + 1) // 2
    middle_number = sorted_numbers[middle_index - 1]
    print(middle_number)


N = int(input())
numbers = list(map(int, input().split()))

find_middle_number(numbers)
