print ("Exam_Results")
name = str(input("Enter your first_name:"))
marks = int(input("Enter Your Marks:"))
if marks==35:
    print ("congratulations" ,name)
    print("you are promoted for next chance!, Marks:",marks)
elif marks>35:
    print ("congratulations" ,name)
    print ("You passes the exam")
    if marks >=75 and marks <85:
        print ("congratulations" ,name)
        print ("You got good score! Marks:",marks)
    elif marks >=85 and marks <95:
        print ("congratulations" ,name)
        print ("you got excellent score! Marks:",marks)
    elif marks>=95:
        print ("congratulations" ,name)
        print ("you are topper! Marks:",marks)
    elif marks >+36 and marks <+74:
        print ("congratulations" ,name)
        print ("you passed with average score, Marks:",marks)
else:
    print ("better luck next time!")
    print("you failed the exam, Marks:",marks)
input ();
