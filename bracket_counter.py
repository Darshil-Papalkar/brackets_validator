import re
from typing import Optional


def bracket_counter(bracket:str, strip: Optional[bool] = False)-> bool:
    """Checks if a given sequence of brackets is balanced (i.e., brackets are balanced).

    Bracktes taken into account are ()[]{}
    Optionally strips non-bracket characters from the input string.

    Parameters
    ----------
    bracket : str
        The input string with brackets.
    strip : Optional[bool], optional
        Whether to strip all non-bracket characters from the input string , by default False

    Returns
    -------
    bool
        `True` if input is balanced, `False` if not.
    """
    brackets = ["()", "[]", "{}"]
    
    if strip:
        strip_re = re.compile('[^\(\)\{\}\[\]]')
        bracket = strip_re.sub('', bracket)
    
    while any(pair in bracket for pair in brackets):
        for pair in brackets:
            bracket = bracket.replace(pair,"")
    balanced = not bracket
    
    return f"{bracket} --> {balanced}"


if __name__ == "__main__":
    try:
        for _ in range(int(input("Enter the number of times to run loop "))):
            print(bracket_counter(input()))
    except Exception as e:
        print(e)
