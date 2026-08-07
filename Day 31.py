while True :
    class student :
        def __init__ (self,name,course) :
            self.name = name 
            self.course = course 
        def display (self) :
            print ("Name =", self.name)
            print ("Course =",self.course)
    student1= student (input("\n Enter your name : ") , input ("Enter your course : "))
    student1.display()
    while True :
        choice = input ("Do you want to continue (yes/no) : ").lower().strip()
        if choice == "yes" :
            break
        elif choice == "no" :
            print ("\n thank you !")
            exit ()
        else :
            print ("invalid choice ! plese chooose between yes or no .")
            continue
