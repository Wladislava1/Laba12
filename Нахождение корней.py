# ax**2 +- bx +- c = 0
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
if a == 0:
    print(-c / b)
else:
    if d == 0:
        x = -b / (2*a)
        print(x)
    if d > 0:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(x1,x2)
    if d < 0:
        print('корней нет')
