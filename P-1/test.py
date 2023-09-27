"""test"""


def main():
    number = int(input())
    sum = 0
    multi = 1
    flag = False
    while flag == False:
        sum = number*multi
        if sum >= 1000:
            flag = True
            multi -= 1
        else:
            sum = 0
            multi += 1
    print(number + multi)
main()
