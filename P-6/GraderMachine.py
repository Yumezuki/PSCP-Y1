"""GraderMachine"""


def grader(start, last):
    """function"""
    total = ""
    dli = 0

    if last > start:
        for i in range(start, last + 1):
            if i % 2 == 0:
                total += str(i) + " "
                dli += i

    elif start > last:
        for i in range(start, last - 1, -1):
            if i % 2 == 0:
                total += str(i) + " "
                dli += i

    elif start == last:
        total = start
        dli = start

    print("pass : %s" % total)
    print("Sum : %d" % dli)


grader(int(input()), int(input()))
