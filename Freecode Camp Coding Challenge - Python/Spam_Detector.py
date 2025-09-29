#                                                                     Spam Detector

# Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

#     A represents the country code and can be any number of digits.
#     BBB represents the area code and will always be three digits.
#     CCC and DDDD represent the local number and will always be three and four digits long, respectively.

# Determine if it's a spam number based on the following criteria:

#     The country code is greater than 2 digits long or doesn't begin with a zero (0).
#     The area code is greater than 900 or less than 200.
#     The sum of first three digits of the local number appears within last four digits of the local number.
#     The number has the same digit four or more times in a row (ignoring the formatting characters).

# 1. is_spam("+0 (200) 234-0182") should return False.
# 2. is_spam("+091 (555) 309-1922") should return True.
# 3. is_spam("+1 (555) 435-4792") should return True.
# 4. is_spam("+0 (955) 234-4364") should return True.
# 5. is_spam("+0 (155) 131-6943") should return True.
# 6. is_spam("+0 (555) 135-0192") should return True.
# 7. is_spam("+0 (555) 564-1987") should return True.
# 8. is_spam("+00 (555) 234-0182") should return False.


def is_spam(phone_number):
    country_code_start = phone_number.find('+') + 1
    country_code_end = phone_number.find(' ')
    country_code = phone_number[country_code_start:country_code_end]

    area_code_start = phone_number.find('(') + 1
    area_code_end = phone_number.find(')')
    area_code = phone_number[area_code_start:area_code_end]

    local_number_start = phone_number.find(')') + 2
    local_number = phone_number[local_number_start:].replace("-", "")

    cleaned = phone_number.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")

    if len(country_code) > 2 or (len(country_code) > 0 and country_code[0] != '0'):
        return True

    if int(area_code) > 900 or int(area_code) < 200:
        return True

    first_three_sum = sum(int(digit) for digit in local_number[:3])
    if str(first_three_sum) in local_number[3:]:
        return True

    for i in range(len(cleaned) - 3):
        if cleaned[i] == cleaned[i + 1] == cleaned[i + 2] == cleaned[i + 3]:
            return True

    return False


print(is_spam("+0 (200) 234-0182"))
print(is_spam("+091 (555) 309-1922"))
print(is_spam("+1 (555) 435-4792"))
print(is_spam("+0 (955) 234-4364"))
print(is_spam("+0 (155) 131-6943"))
print(is_spam("+0 (555) 135-0192"))
print(is_spam("+0 (555) 564-1987"))
print(is_spam("+00 (555) 234-0182"))
