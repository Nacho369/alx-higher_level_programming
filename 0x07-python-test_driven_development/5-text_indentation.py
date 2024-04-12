#!/usr/bin/python3

"""Define the function `text_indentation(text)`"""


def text_indentation(text):
    """This function prints a text with 2 new lines after each of
    these characters: ., ? and :

    Args:
        text(str): Text to print with 2 new lines after the given characters

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text_line = ""
    prev_char = ""

    for curr_char in text:
        if prev_char in ".?:\n" and curr_char == " ":
            continue

        if not (curr_char == " " and prev_char in ".?:"):
            text_line += curr_char

        print("{}".format(text_line), end="")
        text_line = ""

        if curr_char in ".?:":
            print("\n")

        prev_char = curr_char
