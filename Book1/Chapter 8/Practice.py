# First 3 problem prove someone has very basic knowledge of pure python programming
def separator(text):
    """"
    This function will separate the uppercase, lowercase letters, numbers and non-alphanumeric signs
    and return 4 list from a single string.
    Example : Input: "BildNW 123!"
             Output: ['BNW', 'ild', '123', '!']
    """
    upper, lower, number, non_alpha = [], [], [], []
    text = text.replace(" ", "")
    for char in text:
        if char.isalnum():
            if char.isdigit():
                number.append(char)
            else:
                if char.islower():
                    lower.append(char)
                else:
                    upper.append(char)
        else:
            non_alpha.append(char)
    
    upper, lower, number, non_alpha = "".join(upper), "".join(lower), "".join(number), "".join(non_alpha)
    
    return [upper, lower, number, non_alpha]


def position_exchanger(text):
    """"
    This function will replace 2nd character by first character, 4th by 3rd, 6th by 5th, etc.
    Example: Input: BildNW 123!
            Output: iBdlWN1 32!
    """
    li = list()
    length = len(text)
    even_length = (length // 2)*2
    for char in range(0, even_length, 2):
        try:
            li.append(text[char + 1])
            li.append(text[char])
        except:
            pass
    if length != even_length:
        li.append(text[even_length])
    return "".join(li)


def palindrome_checker(text):
    """
    This function will check the text is palindrome or not. Palindrome means that the actual text and the reverse
    text are equal.
    Note: If you find someone who used for loop for this problem, it will be not good !
    """
    li = []
    li[:0] = text
    li.reverse()
    reversed_text = "".join(li)
    return text == reversed_text


# Problem that prove almost 30% knowledge of pure python
def replace(text=None):
    import re
    """
    This function will replace "/" by "-", and reformat the date.
    Example: Input: "22/04/2022, 23/02/2021, 31/02/2020"
            Output: "2022-04-22, 2021-02-23, 2020-02-31"
    """
    
    text = "22/04/2022, 23/02/2021, 31/02/2020"
    pattern = re.compile(r"(\d+)/(\d+)/(\d+)")
    result = pattern.sub(r"\g<3>-\g<2>-\g<1>", text)
    return result


if __name__ == "__main__":
    testing_text = "Write your testing text here!"
    # values = separator("BildNW 123!")
    # print(values)
    # changed = position_exchanger("BildNW 123!")
    # print(changed)
    # pal = palindrome_checker("madam")
    # print(changed)
    # formatted = replace()
    # print(formatted)
    