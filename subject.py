import json
def subject_menu():
    while True:
        print("\n====subject management system====")
        print("1,add subject")
        print("2,show subject")
        print("3,search subject")
        print("4,update subject")
        print("5,delete subject")
        print("6,exit")
        
        choice=input("enter subject choice(1-6):")
        
        if choice=="1":
            add_subject()
            
        elif choice=="2":
            show_subject()
            
        elif choice=="3":
            search_subject()
            
        elif choice=="4":
            update_subject()
            
        elif choice=="5":
            delete_subject()
            
        elif choice=="6":
            break
def load_subjects():
    try:
        file=open("subjects.json","r")
        subjects=json.load(file)
        file.close()
        return subjects
    except:
        return[] 
    
def save_subjects(subjects):
    file=open("subjects.json","w")
    json.dump(subjects,file,indent=4)
    file.close()
       
def add_subject():
    subjects=load_subjects()
    id=input("enter subject id:")
    for subject in subjects:
        if subject["id"]==id:
            print("this subject id already exits.")
            return
    name=input("enter subject name:")
    subject_class=input("enter class:")
    teacher_id=input("enter teacher id:")
     
    subject={
        "id":id,
        "name":name,
        "class":subject_class,
        "teacher_id":teacher_id
    }
    
    subjects.append(subject)
    save_subjects(subjects)
    print("subject added successfully.")
    
def show_subject():
    subjects=load_subjects()
    if len(subjects)==0:
        print("no subject found.")
        return
    print("_"*50)
    print(f"{'id':<15}{'name':<15}{'student_class':<10}{'teacher_id':<10}")
    print("_"*50)
    for subject in subjects:
        print("_"*50)
        print(f"{subject['id']:<15}{subject['name']:<15}{subject['class']:<10 }{subject['teacher_id']:<10}")
        print("_"*50)
    
def search_subject():
    subjects=load_subjects()
    search_id=input("enter search subject id:")
    found=False
    for subject in subjects:
        if subject["id"]==search_id:
            print("----------------------")
            print("id:",subject["id"])
            print("name:",subject["name"])
            print("class:",subject["class"])
            print("teacher_id:",subject["teacher_id"])
            found=True
            break
        if not found:
            print("subject not found.")
    
def update_subject():
    subjects=load_subjects()
    update_id=input("enter subject id to update:")
    found=False
    for subject in subjects:
        if subject["id"]==update_id:
            subject["name"]=input("enter new subject name:")
            subject["class"]=input("enter new class:")
            subject["teacher_id"]=input("enter new teacher id:")
            save_subjects(subjects)
            found=True
            break
        if not found:
            print("subject not found.")
    
def delete_subject():
    subjects=load_subjects()
    delete_id=input("enter subject id to delete:")
    found=False
    for subject in subjects:
        if subject["id"]==delete_id:
            print("subject found")
            print("name:",subject["name"])
            print("class:",subject["class"])
            print("teacher_id:",subject["teacher_id"])
            confirm=input("Are you sure?(y/n):")
            if confirm.lower()=="y":
                subjects.remove(subject)
                save_subjects(subjects)
                print("subject delete successfully.")
                found=True
                break
            if not found:
                print("subject not found.")