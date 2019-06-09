base = float(input())
height = float(input())

# ВАРИАНТ 1

def triangle_area(b, h):
    area = (b*h)/2
    return area

print(f"{triangle_area(base, height):.12g}")

print("++++"*10)

# ВАРИАНТ 2

def triangle_area(b, h):
    area = (b*h)/2
    return area

result = triangle_area(base, height)

print(f"{result:.12g}")

'''' решение
5
6
15
++++++++++++++++++++++++++++++++++++++++
15
'''