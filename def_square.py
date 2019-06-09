n = int(input())

# вариант 1


def print_dashes(num):
    print("-"*(num*2))


def print_body(number):
    for i in range(1, number - 1):
        print("-" + "\\/"*int((2*number-2)/2) + "-")

print_dashes(n)
print_body(n)
print_dashes(n)


print("--"*2)

# вариант 2


def print_dashes(num):
    print("-"*(num*2))


def print_body(number):
    print("-" + "\\/"*int((2*number-2)/2) + "-")

print_dashes(n)
for i in range(1, n-1):
    print_body(n)
print_dashes(n)


''' решение == изход
--------
-\/\/\/-
-\/\/\/-
--------
----
--------
-\/\/\/-
-\/\/\/-
--------
'''