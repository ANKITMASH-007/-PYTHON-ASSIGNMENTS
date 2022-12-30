# this program is to create multilevel inheritence

class A:
    def ca(Self):
        print("This is class A")

class B(A):
    def cb(Self):
        print("This is class B")

class C(B):
    def cc(Self):
        print("This is class C")


obj=C()
obj.ca()