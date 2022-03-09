import random


def solve_equation(a, b, c):
    """Найти корни квадратного уравнения"""
    if 0 not in (a, b, c):  # Ни один из коэф-в не равен нулю
        D = (b**2)-4*a*c
        if D<0:
            return "Корней нет"
        elif D == 0:
            return -b/(2*a)
        else:
            x1 = -b+(D*0.5)/(2*a)
            x2 = -b-(D*0.5)/(2*a)
            return x1, x2
    elif a==0 and b==0 and c==0:  # Все коэф-ты равны нулю
        return "∞"
    else:  # Частные случаи
        if a==0 and b!=0:
            return -c/b
        elif b==0 and c<=0 and a!=0:
            return (-c/a)**0.5
        elif c==0 and a!=0:
            return -b/a
        elif (a==c==0) or (b==c==0):
            return 0
    return "Корней нет"


def get_color():
    """Угадать цвет (экспоненциальное распределение)"""
    x = random.expovariate(lambd=1)
    if x >= 0.5:
        return "Синий цвет"
    elif x >= 0.2:
        return "Зеленый цвет"
    else:
        return "Красный цвет"