# Given an array, return the second largest distinct number.

# 1. second_largest([1, 2, 3, 4]) should return 3.
# 2. second_largest([20, 139, 94, 67, 31]) should return 94.
# 3. second_largest([2, 3, 4, 6, 6]) should return 4.
# 4. second_largest([10, -17, 55.5, 44, 91, 0]) should return 55.5.
# 5. second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]) should return 0.

def second_largest(arr):
    distinct_numbers = set(arr)
    sorted_numbers = sorted(distinct_numbers, reverse=True)
    return sorted_numbers[1]

# Test cases
print(second_largest([1, 2, 3, 4]))
print(second_largest([20, 139, 94, 67, 31]))
print(second_largest([2, 3, 4, 6, 6]))
print(second_largest([10, -17, 55.5, 44, 91, 0]))
print(second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]))