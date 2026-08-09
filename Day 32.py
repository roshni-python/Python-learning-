class Student :
    college = "Daviet"
    def __init__ (self,name,course) :
        self.name = name
        self.course = course 
    def display (self  ) :
        print ("Name =",self.name)
        print ("course =", self.course)
        print ("College =",self.college )
student1 = Student (input ("Enter first  student  name :") , input("Enter first student  course :"))
student2 = Student (input("Enter second student name :") , input ("Enter second student course :"))
student1.display()
print()
student2.display()
