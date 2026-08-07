import json

def teacher_menu():
    while True:
        print("\n====teacher management system====")
        print("1,add teacher")
        print("2,show teacher")
        print("3,search teacher")
        print("4,update teacher")
        print("5,delete teacher")
        print("6,break")
        
        choice=input("enter your choice(1-6):")
        
        if choice=="1":
            add_teacher()
        
        elif choice=="2":
            show_teachers()
        
        elif choice=="3":
            search_teachers()
            
        elif choice=="4":
            update_teacher()
            
        elif choice=="5":
            delete_teacher()
            
        elif choice=="6":
            break
        else:
            print("Invalid choice")
            
def load_teacher():
    try:
        file=open("teachers.json","r")
        teachers=json.load(file)
        file.close()
        return teachers
    except:
        return[]
    
def save_teachers(teachers):
    file=open("teachers.json","w")
    json.dump(teachers,file,indent=4)
    file.close()
    
def add_teacher():
    teachers=load_teacher()
    id=input("enter id:")
    for teacher in teachers:
        if teacher["id"]==id:
            print("this id already exits")
            return
    name=input("enter teacher name:")
    subject=input("enter subject")
    department=input("enter department")
    
    teacher={
        "id":id,
        "name":name,
        "subject":subject,
        "department":department
    }
    teachers.append(teacher)
    save_teachers(teachers)
    print("teacher added successfully")
    
def show_teachers():
    teacher=load_teacher()
    if len(teacher)==0:
        print("no teacher found.")
        return
    print("_"*50)
    print(f"{'id':<10}{'name':<10}{'subject':<15}{'department':<10}")
    print("_"*50)
    
    for teacher in teacher:
        print(f"{teacher['id']:<10}{teacher['name']:<10}{teacher['subject']:<15}{teacher['department']:<10}")
        print("_"*50)
    
def search_teachers():
    teachers=load_teacher()
    search_id=input("enter teacher id:")
    found=False
    for teacher in teachers:
        if teacher["id"]==search_id:
            print("----------------")
            print("id:",teacher["id"])
            print("name:",teacher["name"])
            print("subject:",teacher["subject"])
            print("department:",teacher["department"])
            found=True
            break
        if not found:
            print("teacher not found.")
    
def update_teacher():
    teachers=load_teacher()
    update_id=input("enter teacher id to update:")
    found=False
    for teacher in teachers:     
        if teacher["id"]==update_id:
            teacher["name"]=input("enter new name:")
            teacher["subject"]=input("enter new subject:")
            teacher["department"]=input("enter new department:")
            save_teachers(teachers)
            found=True
            break
        if not found:
            print("teacher not found.")
    
def delete_teacher():
    teachers=load_teacher()
    delete_id=input("enter teacher id to delete:")
    found=False
    for teacher in teachers:
        if teacher["id"]==delete_id:
            print("teacher found'")
            print("name:",teacher["name"])
            print("subject:",teacher["subject"])
            print("department:",teacher["department"])
            confirm=input("Are you sure?,(y/n):")
            if confirm.lower()=="y":
                teachers.remove(teacher)
                save_teachers(teachers)
                print("teacher delete successfully.")
                found=True
                break
            if not found:
                print("teacher not found.")