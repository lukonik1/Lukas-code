def find_max(list):
    result = list[0]
    for number in list:
        if number > result:
            result = number
    return result