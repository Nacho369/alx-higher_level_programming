#!/usr/bin/python3
def magic_string():
    magic_string.call_count = getattr(magic_string, 'call_count', 0) + 1
    return 'BestSchool, ' * (magic_string.call_count - 1) + "BestSchool"
