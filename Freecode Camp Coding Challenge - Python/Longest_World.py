    #                                                         Longest Word

    # Given a sentence, return the longest word in the sentence.

    # Ignore periods (.) when determining word length.
    # If multiple words are ties for the longest, return the first one that occurs.

# 1. get_longest_word("coding is fun") should return "coding".
# 2. get_longest_word("Coding challenges are fun and educational.") should return "educational".
# 3. get_longest_word("This sentence has multiple long words.") should return "sentence".

import re

def get_longest_word(sentence):
     return max(sentence.replace('.', '').split(), key=len)        # Works for ignoring the periods only       
                
    # return max(re.sub(r'[^\w\s]', '', sentence).split(), key=len)   # Works for ignoring all punctuation or special characters. 



print(get_longest_word("coding is fun"))
print(get_longest_word("Coding challenges are fun and educational."))
print(get_longest_word("This sentence has multiple long words."))

# print(get_longest_word("Hello World!!"))