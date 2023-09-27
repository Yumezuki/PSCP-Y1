"""ValidVar"""


def validvar(value):
    """function"""
    for _ in range(value):
        txt = input()
        if txt in ["if", "else", "elif", "while", "for", "True", \
                   "False", "continue", "break", "return", "is", \
                    "in", "and", "or", "from", "as", "pass", \
                    "not", "def", "None",] \
                    or txt.isidentifier() == False or txt.isspace() == True:
            print("Invalid")
        else:
            print("Valid")


validvar(int(input()))
