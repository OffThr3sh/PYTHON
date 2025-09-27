# -----------------------------------------------------------------  Sentence Capitalizer ---------------------------------------------------------------------------


# Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

#     All other characters should be preserved.
#     Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).


# ----------------------------------------------------  Tests  ------------------------------------------------------------------------------------------------------

# Waiting: 1. capitalize("this is a simple sentence.") should return "This is a simple sentence.".
# Waiting: 2. capitalize("hello world. how are you?") should return "Hello world. How are you?".
# Waiting: 3. capitalize("i did today's coding challenge... it was fun!!") should return "I did today's coding challenge... It was fun!!".
# Waiting: 4. capitalize("crazy!!!strange???unconventional...sentences.") should return "Crazy!!!Strange???Unconventional...Sentences.".
# Waiting: 5. capitalize("there's a space before this period . why is there a space before that period ?") should return "There's a space before this period . Why is there a space before that period ?".

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

import re

def capitalize(paragraph):
    sep_words = re.split(r'([.?!]+)', paragraph)
    
    result = []
    capitalize_next = True

    for words in sep_words:
        if not words:
            continue

        if re.match(r'[.?!]+', words):
            result.append(words)
            capitalize_next = True
        else:
            if capitalize_next:
                # scan for first alphabetic character
                chars = list(words)
                for i, ch in enumerate(chars):
                    if ch.isalpha():
                        chars[i] = ch.upper()
                        break
                words = "".join(chars)
                capitalize_next = False
            result.append(words)

    return "".join(result)


print(capitalize("this is a simple sentence."))