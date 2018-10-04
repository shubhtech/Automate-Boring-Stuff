import re

text = input()
text2 = input("type something you want to remove from previous string(optional)")

def regex_strip(text, remove=None):
    if remove is not None:
        remove_regex = re.compile(remove)        # remove desired text from input
        text = remove_regex.sub("", text)

    strip_regex = re.compile(r"[\S]+")    #make regex for space
    mo = strip_regex.search(text)         # seearch for space in input text
    striped_text = mo.group()
    return striped_text

    
print(regex_strip(text))
print(regex_strip(text, text2))