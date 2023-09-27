"""FizzBuzz"""


def fizzbuzz(num):
    """function"""
    for numby in range(1, num + 1):
        if numby % 15 == 0:
            print(str(numby).replace(str(numby), "FizzBuzz"))
        elif numby % 3 == 0:
            print(str(numby).replace(str(numby), "Fizz"))
        elif numby % 5 == 0:
            print(str(numby).replace(str(numby), "Buzz"))
        else:
            print(numby)


fizzbuzz(int(input()))
