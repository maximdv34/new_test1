from math import sqrt
a, b, c  = input('Введите числа a, b, c через запятую: ').strip().split(',')
a, b, c = int(a), int(b), int(c)
d = b*b - 4*a*c
if d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
else:
    x1 = -(-b - sqrt(-d)) / (2 * a)
    x2 = -(-b + sqrt(-d)) / (2 * a)

print(f'x1 = {x1}\nx2 = {x2}')
