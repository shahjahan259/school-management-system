import json

def attendance_menu():
    while True:
        print("\n====attendance management====")
        print("1,add attendance")
        print("2,show attendance")
        print("3,search attendance")   
        print("4,update attendance")
        print("5,delete attendance")
        print("6,Exit")
        
        choice=input("Enter your choice(1-6):")
        
        if choice=="1":
            add_attendance()
            
        elif choice=="2":
            show_attendance()
            
        elif choice=="3":
            search_attendance()
            
        elif choice=="4":
            update_attendance()
            
        elif choice=="5":
            delete_attendance()
        elif choice=="6":
            break
        else:
            print("Invalid choice")
def load_attendance():
    try:
        file=open("attendances.json","r")
        attendances=json.load(file)
        file.close()
        return attendances  
    except:
        return[]
    
def save_attendance(attendances):
    file=open("attendances.json","w")
    json.dump(attendances,file,indent=4)
    file.close()
    
def add_attendance():
    attendance=load_attendance()
    student_id=input("enter student id:")
    date=input("enter present date:")
    status=input("enter status:")
    
    new_attendance={
        "student_id":student_id,
        "date":date,
        "status":status
    }
    attendance.append(new_attendance)
    save_attendance(attendance)
    print("attendance added successfully.")
    
def show_attendance():
    attendance=load_attendance()
    if len(attendance)==0:
        print("no attendance found")
        return
    print("_"*50)
    print(f"{'student_id':<15}{'date':<20}{'status':<10}")
    print("_"*50)
    for attendance in attendance:
        print(f"{attendance['student_id']:<15}{attendance['date']:<20}{attendance['status']:<10}")
        print("_"*50)
        
    
def search_attendance():
    attendance=load_attendance()
    student_id=input("enter student_id:")
    found=False
    
    for attendance in attendance:
        print("----------------------------------")
        print("date:",attendance["date"])
        print("status:",attendance["status"])
        found=True
        break
    
    if not found:
        print("attendance is not found.")
    
def update_attendance():
    attendance=load_attendance()
    student_id=input("enter studant id:")
    date=input("enter date")
    found=False
    for attendance in attendance :
        if attendance["student_id"]==student_id and attendance["date"]==date:
            print("-----------------------------------")
            attendance["status"]=input("enter new status:")
            save_attendance(attendance)
            found=True
            break
    if not found:
        print("attendance not found.")
    
def delete_attendance():
    attendances=load_attendance()  
    student_id=input("enter student id:")  
    date=input("enter date:")
    found=False
    for attendance in attendances:
        if attendance["student_id"]==student_id :
            print("found student_id.") 
            print("date:",attendance["date"])
            print("status:",attendance["status"]) 
            
            confirm=input("Are you sure?(y/n):")  
            if confirm.lower()=="y":
                attendances.remove(attendance)
                save_attendance(attendances)
                print("attendance delete successfully.")
                found=True
                break
            if not found:
                print("attendance not found.")