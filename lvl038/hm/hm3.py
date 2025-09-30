def string_to_int_manual(s):
    num = 0
    for char in s:
        num = num * 10 + (ord(char) - ord('0'))
    return num
