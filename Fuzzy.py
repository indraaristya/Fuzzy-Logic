from __future__ import division


class Triangle(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def fuzzification(self, x):
        if x <= self.a:
            return 0
        elif self.a < x < self.b:
            return (x - self.a) / (self.b - self.a)
        elif x == self.b:
            return 1
        elif self.b < x < self.c:
            return (self.c - x) / (self.c - self.b)
        else:
            return 0


class Trapezoid(object):

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def fuzzification(self, x):
        if x <= self.a:
            return 0
        elif self.a < x < self.b:
            return (x - self.a) / (self.b - self.a)
        elif self.b <= x and self.c >= x:
            return 1
        elif self.c < x < self.d:
            return (self.d - x) / (self.d - self.c)
        else:
            return 0



class defuzzification(object):

    def __init__(self, nk):
        self.nk = nk

    def sugeno(self, x):
        result = 0
        temp = 0
        for i in range(len(self.nk)):
            result += (self.nk[i] * x[i])
            temp += x[i]
        return result / temp
