# проверка дали едно число е положително, отрицотелно или 0

n = float(input())


def sign_of_integer(number):
    if number < 0:
        print('The number ' + str(number) + ' is negative.')
    elif number > 0:
        print(f'The number  {number}  positive.')
    else:
        print('The number 0 is zero.')


sign_of_integer(n)

