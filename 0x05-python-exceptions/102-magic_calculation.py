#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for code in range(1, 3):
        try:
            if code > a:
                raise Exception('Too far')
            result += a ** b / code
        except Exception:
            result = b + a
            break
    return result
