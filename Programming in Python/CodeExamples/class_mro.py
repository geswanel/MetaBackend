class A:
    def a(self):
        print("a: Inside class A")
    
    def b(self):
        print("b: Inside class A")
    
    def c(self):
        print("c: Inside class A")
    

class B:
    def b(self):
        print("b: Inside class B")
    
    def c(self):
        print("c: Inside class B")

# Multiple inheritance
class C(B, A):
    def c(self):
        print("c: Inside class C")

print("C class MRO")
c = C()
c.a()
c.b()   # order C -> B -> A

# Hybrid inheritance from multiinherited class
class D(C):
    pass


print("D class mro")
d = D() # D -> C -> B -> A
d.c()
d.b()
d.a()

# Direct superclass from different levels
class F(C, A):
    pass

print(F.mro()) # F -> C -> B -> A

# Failed mro
# class E(A, C):  # cannot create consistent mro. E -> A -> C -> B -> A (A before C cannot be because of C3 algo)
#     pass


# Complicated hybrid inheritance
# A, B, G - 0 level
#  H,  I - 1 level
# J - 2 level inherited from 1 and 0 level
class G:
    pass

class H(A, B):
    pass

class I(B, G):
    pass

class J(I, H, G):   # J -> I -> H -> A -> B -> G
    a = 5
    pass

print(J.mro())