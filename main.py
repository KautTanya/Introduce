"""Introduce"""


class A:
    """A"""
    def introduce(self):
        """info"""
        return "Class A"


class B(A):
    def introduce(self):
        """info"""
        return "Class B"


class C(A):
    pass
    # def introduce(self):
    #     """info"""
    #     return "Class C"


class D(B, C):
    pass
    # def introduce(self):
    #     """info"""
    #     return "Class D"


a = A()
b = B()
c = C()
d = D()

print(a.introduce())
print(b.introduce())
print(c.introduce())
print(d.introduce())
