while True :
    try :
        import math 
        number = int (input ("\n Enter a number :"))
        result = math.sqrt (number)
        print ("Square Root =",result)
        print ("operation successfull .")
        while True : 
            choice = input ("Do you want to continue ? (yes/no) :").lower().strip()
            if choice == "yes" :
                break 
            elif choice == "no" :
                print ("Thank You !")
                exit ()
            else :
                print ("Invalid choice ! plese choose between yes or no .")     
    except ValueError :
        print ("Error ! plese enter numbers only.")
    
