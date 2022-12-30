# this program we will learn method overridding

class A:
    def display(Self):
        print("Parent Function")

class B(A):
    def display(Self):
        super().display()
        print("Child Function")
        
obj=B()
obj.display()