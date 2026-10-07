"""Pola figur płaskich."""
import math


def circle_area(r):
    """Pole koła o promieniu r (użyj math.pi)."""
    raise NotImplementedError


def rectangle_area(a, b):
    """Pole prostokąta a × b."""
    raise NotImplementedError


def triangle_area(a, b, c):
    """Pole trójkąta ze wzoru Herona: p = (a+b+c)/2,  P = sqrt(p(p-a)(p-b)(p-c)).

    Gdy z boków nie da się zbudować trójkąta, zwraca None.
    """
    raise NotImplementedError
