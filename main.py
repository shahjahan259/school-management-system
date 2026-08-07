from login import login
from student import student_menu
from teacher import teacher_menu
from subject import subject_menu
from marks import mark_menu
from attendance import attendance_menu
from fee import fee_menu
if login():
    while True:
        print("\n====school management system====")
        print("1,student management")
        print("2,teacher management")
        print("3,subject management")
        print("4,mark management")
        print("5,attendance")
        print("6,fee collection")
        print("7,log out")
        print("8,exit")
        
        choice=input("enter your choice(1-8):")
    
        if choice=="1":
            student_menu()
        elif choice=="2":
            teacher_menu()
        elif choice=="3":
            subject_menu()
        elif choice=="4":
            mark_menu()
        elif choice=="5":
            attendance_menu()
        elif choice=="6":
            fee_menu()
        elif choice=="7":
            print("logged out successfully.")
            break
        elif choice=="8":
            print("Thank you for using school management system.")
            break
        else:
            print("Invalid choice")
else:
    print("access Denied")
    
    