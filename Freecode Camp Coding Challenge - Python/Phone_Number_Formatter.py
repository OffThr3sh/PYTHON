            #                                         Phone Number Formatter

            # Given a string of ten digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".
            
            # 1. format_number("05552340182") should return "+0 (555) 234-0182".
            # 2. format_number("15554354792") should return "+1 (555) 435-4792".


def format_number(number):
    country_code = number[:-10]
    area_code = number[-10:-7]
    local_number_first = number[-7:-4]
    local_number_last = number[-4:]

    return f"+{country_code} ({area_code}) {local_number_first}-{local_number_last}"


print(format_number("05552340182"))
print(format_number("15554354792"))