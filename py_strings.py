# pylint: disable=C0114
import string

def reverse(text: str) -> str:
    """
    Return the 'text' backwards.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The text written backwards.
    """
    return text[::-1]


def first_to_upper(text: str) -> str:
    """
    Changes each first character of the word to uppercase.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The modified text
    """
    #wszystkie seperatory slow powinny byc zdefiniowane w sign
    sign=  ".-;',"
    s = ''
    if(len(text)<= 0):
        return s
    else:
        c = text[0].upper()
        change = 0
        for i in range(1,len(text)):
            if(change == 1):
                s = s + c
                c = text[i].upper()
                change = 0
            else:
                c = c+text[i]
            if(text[i] == " " or text[i] == "\n" or text[i] =="\t" or text[i] in sign):
                change = 1   
        s = s+c
        return s
        



def count_vowels(text: str) -> int:
    """
    Counts number of vovels in the text.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    inp
        Number of vowels.
    """
    vowels = "aeiouóÓąĄęĘAEIOUyY"
    return len([char for char in text if char in vowels])


def sum_digits(text: str) -> int:
    """
    Finds all digitts in the text and returns its sum.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int
        Sum of all digits in the text.
    """
    count = 0
    for char in text:
        if char.isdigit():
            count = count+int(char)  
    return count


def search_substr(text: str, sub: str) -> int:
    """
    Search for sub(string) in the text. Returns the position or None.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int or None
        Position of the sub(string) or None.
    """
    result = text.find(sub)
    if(result == -1):
        result = None
    return result