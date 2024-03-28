import random as rn
def shuffle(password):
    temp_password = list(password)
    rn.shuffle(temp_password)
    return ''.join(temp_password)

digit_1 = chr(rn.randint(48,57))
digit_2 = chr(rn.randint(48,57))
uppercase_letter_1 = chr(rn.randint(65,90))
uppercase_letter_2 = chr(rn.randint(65,90))
lowercase_letter_1 = chr(rn.randint(97,122))
lowercase_letter_2 = chr(rn.randint(97,122))
symbols_1 = chr(rn.randint(33,47))
symbols_2 = chr(rn.randint(33,47))
password = digit_1 + digit_2 + uppercase_letter_2 + uppercase_letter_1 + lowercase_letter_1 + lowercase_letter_2 + symbols_2 + symbols_1

print(shuffle(password))