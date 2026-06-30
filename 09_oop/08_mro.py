# Method Resolution Order(mro)
class A:
    label = "A: Base Class"

class B(A):
    label = "B: Masala blend (inherited A)" #overwrites label

class C(A):
    label = "C: Herbal blend (inherited A)" # B: overwrites label

class D(B, C): #inheriting B and C
    pass  #it doesn't have any label so it will in inherited class

cup = D()
print(D.label) # B: Masala blend (inherited A)
# it picks the property from the first inhereted class so position matters.

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# inhertance chain : D -> B -> C -> A 