class Person :
    def __init__ (self , name , age  ) :
        self.name = name 
        self.age = age   
    def  display (self) :
        print ("Name =",self.name)
        print ("Age =",self.age)
class Student (Person) :
    def __init__( self , name , age , course) :
         super().__init__(name , age) 
         self.course = course 
    def display (self) :
        super().display ()
        print ("Course =",self.course)
while True :
     name = input ("Enter first student name :")
     if ''.join(name.split()).isalpha() : 
          print ("name Valid !")
          break
     else :
         print ("invalid name !")
         continue 
while True :
        try :
            age = int(input("Enter age :"))
            if age >= 100 :
                print ("Age should be less then 100.")
                continue 
            elif age <= 10 :
                print ("Age should be more then 10.")
                continue
            else :
                print ("Age Valid !")
                break
        except ValueError :
            print ("Invalid age ! ")
course = input("Enter course :")
student1= Student (name , age , course)
while True :
     name = input ("\n Enter second student name :")
     if ''.join(name.split()).isalpha() :
         print ("name valid !")
         break 
     else :
         print ("Invalid name !")
         continue
while True :
    try :
        age = int(input("Enter age :"))
        if age >= 100 :
            print ("Age should be less then 100.")
            continue
        elif age <= 10 :
            print ("Age should be more then 10. ")
            continue
        else :
            print ("Age valid !")
        break
    except ValueError :
        print ("Invalid age !")
course = input ("Enter course :")
student2 = Student (name , age , course )
student1.display()
student2.display()
