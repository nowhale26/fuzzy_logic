from typing import Union, List, Any, Tuple


def not_a(f: list) -> list[Union[int, Any]]:
    a = []
    for el in f:
        a.append(1 - el)
    return a


def very_a(f: list) -> list[Any]:
    a = []
    for el in f:
        a.append(el ** 2)
    return a


def mol_a(f: list) -> list[Union[float, Any]]:
    # more or less
    a = []
    for el in f:
        a.append(el**0.5)
    return a


def a_or_b(f1: list, f2: list) -> tuple[list, bool]:
    a = []
    i = 0
    marker = False
    if len(f1) > len(f2):
        c = f1
        f1 = f2
        f2 = c
        marker = True
    for el in f1:
        try:
            a.append(min(el, f2[i]))
        except:  # if went beyond the function definition
            a.append(0)
        i += 1
    return a, marker


def a_and_b(f1: list, f2: list) -> tuple[list, bool]:
    a = []
    i = 0
    marker = False
    if len(f1) > len(f2):
        c = f1
        f1 = f2
        f2 = c
        marker = True
    for el in f1:
        try:
            a.append(max(el, f2[i]))
        except:
            a.append(0)
        i += 1
    return a, marker
