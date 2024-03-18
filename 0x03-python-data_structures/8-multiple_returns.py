#!/usr/bin/python3


def multiple_returns(sentence):
    tup_ret = ()
    first_ch = ""
    if (len(sentence) == 0):
        first_ch = None
    else:
        first_ch = sentence[0]
    
    str_len = len(sentence)
    tup_ret = (str_len, first_ch)

    return (tup_ret)
