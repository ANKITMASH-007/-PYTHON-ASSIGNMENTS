import pickle
class Student:
     def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

     def disp(self):
        print(f'Name: {self.name} Roll: {self.roll} Marks {self.marks}')
  
with open('Student. dat', mode= 'wb') as f:
        stu1 = Student('Astha', 101, 88)
        pickle.dump(stu1,f)
        print ('Pickling Done!!')
        stu2 = Student('Amit', 101, 87)
        pickle.dump(stu2,f)
        print ('Pickling Done!!')
        stu3 = Student('Ankit', 101, 91)
        pickle.dump(stu3,f)
        print ('Pickling Done!!')

with open ('student. dat',mode='rb') as f:
        obj1= pickle.load(f)
        obj2 = pickle.load(f)
        obj3= pickle.load(f)
        print('Unpickling Done!!')
        #to print name with the highest marks
        if(obj1.marks>obj2.marks):
            