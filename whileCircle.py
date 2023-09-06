"""
    while循环
"""
import random


def get_sum1_100():
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    return sum


def guess_number():
    num = random.randint(1, 100)
    flag = True
    while flag:
        guess_number = int(input("请猜出您的数字"))
        if guess_number == num:
            flag = False
            print(f'您猜对了，数字为:{guess_number}-{num}')
        else:
            if guess_number > num:
                print(f'您猜大了:{guess_number}')
            else:
                print(f'您猜小了:{guess_number}')


def print9_9(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(f'{i} * {j} = {i*j}', end='\t')
            j += 1
        print()
        i += 1


if __name__ == '__main__':
    i = 0
    while i < 10:
        print(i)
        i += 1
    sum = get_sum1_100()
    print(f'1-100的和：{sum}')
    # guess_number()
    print9_9(9)
