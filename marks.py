import json

def mark_menu():
    while True:
        print("\n====marks management====")
        print("1,add mark")
        print("2,show mark")
        print("3,search mark")
        print("4,update mark")
        print("5,delete mark")
        print("6,exit")
        
        choice=input("enter choice(1-6):")
        if choice=="1":
            add_mark()
            
        elif choice=="2":
            show_mark()
            
        elif choice=="3":
            search_mark()
            
        elif choice=="4":
            update_mark()
            
        elif choice=="5":
            delete_mark()
            
        elif choice=="6":
            break
        
def load_marks():
    try:
        file=open("marks.json","r")
        marks=json.load(file)
        file.close()
        print(marks)
        print(type(marks))
        return marks
    except:
        return[]
    
def save_marks(marks):
    file=open("marks.json","w")
    json.dump(marks,file,indent=4)
    file.close()
    
def add_mark():
    marks=load_marks()
    student_id=input("enter student_id:")
    subject_id=input("enter subject_id:")
    exam=input("enter exam:")
    mark=int(input("enter mark:"))
    new_mark={
        "student_id":student_id,
        "subject_id":subject_id,
        "exam":exam,
        "marks":mark,
    } 
    print(marks)
    print(type(marks))
    marks.append(new_mark)
    save_marks(marks)
    print("marks added successfully.") 
    
def show_mark():
    marks=load_marks()
    if len(marks)==0:
        print("no marks found.")
        return
    print("_"*50)
    print(f"{'student_id':<10}{'subject_id':<10}{'exam':<15}{'mark': <10}")
    print("_"*50)
    for mark in marks:
        print(f"{mark['student_id']:<10}{mark['subject_id']:<10}{mark['exam']:<15}{mark['marks']:<10}")
        print("_"*50)
        
    
def search_mark():
    marks=load_marks()
    student_id=input("enter student_id:")
    subject_id=input("enter subject id:")

    found=False
    
    for mark in marks:
        if mark["student_id"]==student_id and mark["subject_id"]==subject_id:
            
            print("----------------------------------------")   
            print("student_id:",mark["student_id"])
            print("subject_id:",mark["subject_id"])
            print("exam:",mark["exam"])
            print("marks:",mark["marks"])
            found=True
            break
    if not found:
        print("marks not found.")
def update_mark():
    marks=load_marks()
    student_id=input("enter student id to update:")
    subject_id=input("enter subject id to update:")
    found=False
    for mark in marks:
        if mark["student_id"]==student_id and mark["subject_id"]==subject_id:
            print("----------------------------------")
            mark["exam"]=input("enter new exam:")
            mark["marks"]=input("enter new marks:")
            save_marks(marks)
            found=True
            break
    if not found:
        print("marks not found.")
    
def delete_mark():
    marks=load_marks()
    student_id=input("enter student id:")
    subject_id=input("enter subject id:")
    found=False
    for mark in marks:
        if mark["student_id"]==student_id and mark["subject_id"]==subject_id:
            print("found student_id and subject id.")
            print("exam:",mark["exam"]),
            print("mark:",mark["marks"])
            
            confirm=input("Are you sure?(y/n):")
            if confirm.lower()=="y":
                marks.remove(mark)
                save_marks(marks)
                print("marks delete successfully.")
                found=True
                break
            if not found:
                print("marks not found.")