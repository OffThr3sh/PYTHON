#                                                                 String Mirror

#                                 Given two strings, determine if the second string is a mirror of the first.

# A string is considered a mirror if it contains the same letters in reverse order. Treat uppercase and lowercase letters as distinct.Ignore all non-alphabetical characters.

# 1. is_mirror("helloworld", "helloworld") should return False.
# 2. is_mirror("Hello World", "dlroW olleH") should return True.
# 3. is_mirror("RaceCar", "raCecaR") should return True.
# 4. is_mirror("RaceCar", "RaceCar") should return False.
# 5. is_mirror("Mirror", "rorrim") should return False.
# 6. is_mirror("Hello World", "dlroW-olleH") should return True.
# 7. is_mirror("Hello World", "!dlroW !olleH") should return True.

def is_mirror(str1, str2):
    filtered_str1 = ''.join(filter(str.isalpha, str1))
    filtered_str2 = ''.join(filter(str.isalpha, str2))
    return filtered_str1 == filtered_str2[::-1]

print(is_mirror("helloworld", "helloworld"))
print(is_mirror("Hello World", "dlroW olleH"))
print(is_mirror("RaceCar", "raCecaR"))
print(is_mirror("RaceCar", "RaceCar"))
print(is_mirror("Mirror", "rorrim"))
print(is_mirror("Hello World", "dlroW-olleH"))
print(is_mirror("Hello World", "!dlroW !olleH"))