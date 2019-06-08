# проверка дали едно число е положително, отрицотелно или 0

n = float(input())


def number(n1):
    if n1 < 0:
        print('The number ' + str(n1) + ' is negative.')
    elif n1 > 0:
        print('The number ' + str(n1) + ' positive.')
    else:
        print('The number 0 is zero.')


number(n)

