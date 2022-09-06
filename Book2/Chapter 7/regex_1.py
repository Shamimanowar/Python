import re


def search(text=None):
    match = re.search(r'B\w+\s?', text)
    try:
        print(match.group())
    except AttributeError:
        print("No match")


def replace(text=None):
    text = "22/04/2022, 23/02/2021, 31/02/2020"
    pattern = re.compile(r"(\d+)/(\d+)/(\d+)")
    result = pattern.sub(r"\g<3>-\g<2>-\g<1>", text)
    print(result)
    
    
replace()
    