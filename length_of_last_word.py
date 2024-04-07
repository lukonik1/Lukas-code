def length_of_last_word(string):
    s = string.split()
    if not s:
        return 0
    else:
        return len(s[-1])
