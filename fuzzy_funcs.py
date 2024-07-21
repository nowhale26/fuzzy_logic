from math import sqrt, pi, e
from typing import Optional, Union


class Universum(object):
    def __init__(self, l=0, r=10, epsilon=0):
        self.u = [i / (10 ** epsilon) for i in range(l * (10 ** epsilon), (r) * (10 ** epsilon))]


def s_func(u: list,
           a: Optional[int] = None,
           b: Optional[int] = None,
           c: Optional[int] = None) -> list[Union[int, float]]:
    s = []
    if a is None:
        a = u.min()
    if c is None:
        c = u.max()
    if b is None:
        b = (a + c) / 2

    for x in u:
        if x < a:
            s.append(0)
        elif (x >= a) and (x < b):
            j = 2 * ((x - a) / (c - a) ** 2)
            s.append(j)
        elif (x >= b) and (x < c):
            j = 2 * ((x - c) / (c - a) ** 2)
            s.append(1 - j)
        elif x >= c:
            s.append(1)
    return s


def pi_func(u: list,
            a: Optional[int] = None,
            b: Optional[int] = None,
            c: Optional[int] = None) -> list[Union[int, float]]:
    pi_1 = []
    pi_2 = []

    if a is None:
        a = u.min()
    if c is None:
        c = u.max()
    if b is None:
        b = (a + c) / 2

    for x in u:
        if x < c:
            X = [x]
            el = s_func(X, c - b, c - (b / 2), c)
            pi_1.append(el[0])

        elif x >= c:
            X = [x]
            el = s_func(X, c, c + (b / 2), c + b)
            pi_2.append(1 - el[0])

    return pi_1 + pi_2


def t_func(u: list,
           a: Optional[int] = None,
           b: Optional[int] = None,
           c: Optional[int] = None) -> list[Union[int, float]]:
    t = []

    if a is None:
        a = u.min()
    if c is None:
        c = u.max()
    if b is None:
        b = (a + c) / 2

    for x in u:
        if x < a:
            t.append(0)
        elif (x >= a) and (x < b):
            t.append((x - a) / (b - a))
        elif (x >= b) and (x < c):
            t.append((c - x) / (c - b))
        elif x >= c:
            t.append(0)
    return t


def y_func(u: list,
           a: Optional[int] = None,
           b: Optional[int] = None) -> list[Union[int, float]]:
    y = []

    if a is None:
        a = u.min()
    if b is None:
        b = u.max()

    for x in u:
        if x < a:
            y.append(0)
        elif (x >= a) and (x <= b):
            y.append((x - a) / (b - a))
        elif x > b:
            y.append(1)
    return y


def l_func(u: list,
           a: Optional[int] = None,
           b: Optional[int] = None) -> list[Union[int, float]]:
    l = []

    if a is None:
        a = u.min()
    if b is None:
        b = u.max()

    for x in u:
        if x < a:
            l.append(1)
        elif (x >= a) and (x <= b):
            l.append((b - x) / (b - a))
        elif x > b:
            l.append(0)
    return l


def gauss_func(u: list,
               a: Optional[int] = None,
               g: Optional[int] = None) -> list[Union[int, float]]:
    if g is None:
        g = 1
    if a is None:
        a = 0
    return [(1 / (g * sqrt(2 * pi))) * (e ** (-(i - a) ** 2 / (2 * g) ** 2)) for i in u]
