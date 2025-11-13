import re

def count_words(text):
    res = len(re.split(r'\s+', text))

    return res

print('\n' + str(count_words('I love data science')))