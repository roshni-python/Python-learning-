while True :
   try :
       number1 = int (input ("Enter your first number :"))
       number2 = int (input ("Enter your second number :"))
       result = number1 / number2
       print ("Answer=",result)
       print ("calculation successfull")
       while True :
           choice = input ("Do you want to continue ? (yes/no) :").lower().strip()
           if choice == "yes" :
                break
           elif choice == "no" :
                print ("THANK YOU !")
                exit ()
           else :
               print ("Invailid choice !")
               continue
   except ZeroDivisionError :
       print ("Error ! division whith zero is not allowed")
   except ValueError :
        print ("Error ! plese enter numbers only ")
