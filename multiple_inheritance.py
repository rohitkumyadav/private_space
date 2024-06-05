class A:
    v1 = "Welcome to class A"

class B:
    v2 =  "Welcome to class B"

class C(A, B):
    v3 ="Welcome to class C"

c1  = C()
print(c1.v1)
print(c1.v2)
print(c1.v3)