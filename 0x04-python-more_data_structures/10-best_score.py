#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return (None)

    max_key = list(a_dictionary.keys())[0]
    max_score = a_dictionary[max_key]

    for key, val in a_dictionary.items():
        if val > max_score:
            max_score = val
            max_key = key

    return (max_key)
