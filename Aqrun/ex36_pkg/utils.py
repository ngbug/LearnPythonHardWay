# -- coding: utf-8 --
"""
util funcs
"""

def str_input(content):
    """v3 v2 input get string"""
    try:
        input = raw_input
    except Exception:
        pass
    return input(content)
