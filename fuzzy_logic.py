"""
This is the main library file.
The fuzzy set class is described here.
"""
from typing import List, Union, Any, Optional

import fuzzy_funcs
import fuzzy_kvant
import matplotlib.pyplot as plt


class fuzzy_set(object):
    def __init__(self,
                 func_type="empty",
                 l: Optional[int] = None,
                 r: Optional[int] = None,
                 a: Optional[int] = None,
                 b: Optional[int] = None,
                 c: Optional[int] = None,
                 epsilon: int = 0,
                 u: Optional[List] = None):

        if (l is not None) and (r is not None):
            self.universum = fuzzy_funcs.Universum(l, r, epsilon)
        else:
            self.universum = u

        self.a = a
        self.b = b
        self.c = c
        self.type = func_type

        if func_type == "S":
            self.f = fuzzy_funcs.s_func(self.universum.u, self.a, self.b, self.c)
        elif func_type == "t":
            self.f = fuzzy_funcs.t_func(self.universum.u, self.a, self.b, self.c)
        elif func_type == "y":
            self.f = fuzzy_funcs.y_func(self.universum.u, self.a, self.b)
        elif func_type == "L":
            self.f = fuzzy_funcs.l_func(self.universum.u, self.a, self.b)
        elif func_type == "PI":
            self.f = fuzzy_funcs.pi_func(self.universum.u, self.a, self.b, self.c)
        elif func_type == "Gauss":
            self.f = fuzzy_funcs.gauss_func(self.universum.u, self.a, self.b)
        elif func_type == "empty":
            self.f = []
        else:
            self.f = []
            for i in self.universum.u:
                if a != 0:
                    v = ((i + b) / a) ** c
                else:
                    v = ((i + b) / (a + 0.00001)) ** c
                self.f.append(1 / (1 + v))

    def init_params(self) -> int:
        return max(self.f)

    def get_sup(self) -> int:
        return max(self.f)

    def get_inf(self) -> int:
        return min(self.f)

    def alpha_cut(self,
                  alpha: int) -> list:
        # go through the set of values, if less than alpha - 0, if greater or equal - value at point
        f_alpha = []
        for i in self.f:
            if i >= alpha:
                f_alpha.append(i)
            else:
                f_alpha.append(0)
        return f_alpha

    def plot(self) -> None:
        graph = plt.plot(self.universum.u, self.f)
        plt.grid(True)

    def plot_scatter(self) -> None:
        graph = plt.scatter(self.universum.u, self.f, marker='o')
        plt.grid(True)

    def kvant(self,
              kvant_type: str,
              f2: Optional[List] = None) -> None:
        if kvant_type == "not":
            self.f = fuzzy_kvant.not_a(self.f)
        elif kvant_type == "very":
            self.f = fuzzy_kvant.very_a(self.f)
        elif kvant_type == "MOL":
            self.f = fuzzy_kvant.mol_a(self.f)
        elif kvant_type == "or":
            marker = False  # if sets have different sizes, then comparisons will occur on a smaller
            self.f, marker = fuzzy_kvant.a_or_b(self.f, f2.f)
            if marker:
                self.f = f2.f
        elif kvant_type == "and":
            marker = False  # if sets have different sizes, then comparisons will occur on a smaller
            self.f, marker = fuzzy_kvant.a_and_b(self.f, f2.f)
            if marker:
                self.f = f2.f
        else:
            raise TypeError


def plot_show() -> None:
    plt.show()
