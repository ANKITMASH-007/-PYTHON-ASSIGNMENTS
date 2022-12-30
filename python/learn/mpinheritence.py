# this program we wil inherit multiple class in one 

class A:
    def ca(Self):
        print("This is class A")
class B:
    def cb(Self):
        print("This is class B")
class C(A,B):
    def cc(Self):
        print("This is class C")


obj=C()
obj.ca()
obj.cb()
obj.cc()
# hence all the methods are called by one onject this is multiple inheritence