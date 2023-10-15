"""Password"""


def pswd(password):
    """Function"""
    import math

    length = len(password)
    pool = 0
    lower = 0
    upper = 0
    num = 0
    special = 0
    for character in password:
        if character.islower() == True:
            if lower == 0:
                lower += 1
                pool += 26

        elif character.isupper() == True:
            if upper == 0:
                upper += 1
                pool += 26

        elif character.isnumeric() == True:
            if num == 0:
                num += 1
                pool += 10

        else:
            special += 1
            if special == 1:
                pool += 32

    entropy = math.floor(math.log2(pool**length))
    print(entropy)
    print(checker(entropy))


def checker(entropy):
    """Checkmate"""
    if entropy < 28:
        output = "Very Weak"

    elif entropy >= 28 and entropy < 36:
        output = "Weak"

    elif entropy >= 36 and entropy < 60:
        output = "Reasonable"

    elif entropy >= 60 and entropy < 128:
        output = "Strong"

    else:
        output = "Very Strong"

    return output


pswd(input())
