import json
    
def student_menu():
    while True:
        print ("\n====student management====")
        print("1,add student")
        print("2,show student")
        print("3,search student ")
        print("4,update student")
        print("5,delete student")
        print("6,break")
        
        choice=input("enter choice(1-6):") 
        
        if choice=="1":
            add_student()
            
        elif choice=="2":
            show_student()
            
        elif choice=="3":
            search_student()
            
        elif choice=="4":
            update_student()
            
        elif choice=="5":
            delete_students()
            
        elif choice=="6":
            break
        else:
            print("invalid choice")
            
def load_students():

    try:
        file=open("students.json","r")
        students=json.load(file)     
        file.close()
        return students
    except:
        return[]

def save_students(students):
    file=open("students.json","w")
    json.dump(students,file,indent=4)
    file.close()
    
def add_student():
    students=load_students()
    id=input("enter id:")
    for student in students:
        if student["id"]==id:
            print("this id already exits.")
            return
        
    student_class=input("enter class:")
    
    roll=int(input("enter roll"))
    for student in students:
        if student["class"]==student_class and student["roll"]==roll:
            print("this roll already exits")
            return
    name=input("enter name:")
    student={
        "id":id,
        "name":name,
        "roll":roll,
        "class":student_class
    }
    students.append(student)
    save_students(students)
    print("student added successfully")
        
def show_student():
    student=load_students()
    if len(student)==0:
        print("no student found")
        return
    print("-"*50)
    print(f"{'id':<10}{'class':<10}{'roll':<10}{'name':<15}")
    print("-"*50)
    for student in student:
        print(f"{student['id']:<10}{student['class']:<10}{student['roll']:<10}{student['name']:<15}")
        print("-"*50)
        
def search_student():
    students=load_students()
    search_id=input("enter student id:")
    found=False
    for student in students:
        if student["id"]==search_id:
            print("------------")
            print("id:",student["id"])
            print("name:",student["name"])
            print("roll:",student["roll"])
            print("class:",student["class"])
            found=True
            break
    if not found:
        print("student not found")
    
def update_student():
    students=load_students()
    update_id=input("enter student id to update:")
    found=False
    for student in students:
        if student["id"]==update_id:
            student["name"]=input("enter new name:")
            student["roll"]=int(input("enter new roll:"))
            student["class"]=input("enter new class: ")
            save_students(students)
            print("student updated successfully.")
            found=True
            break
    if not found:
        print("student not found.")
    
def delete_students():
    students=load_students()
    delete_id= input("enter student id to delete")
    found= False
    for student in students:
        if student["id"]==delete_id:
            print("student found.")
            print("name:",student["name"])
            print("roll:",student["roll"])
            print("class:",student["class"])
            confirm=input("are you sure?,(y/n):" )
            if confirm.lower()=="y":
                students.remove(student)
                save_students(students)
                print("student delete successfully.")
            found=True
            break
    if not found:
        print("student not found.")
    