import json

def fee_menu():
    while True:
        print("\n====fee collection====")
        print("1,add fee")
        print("2,show fee")
        print("3,search fee")
        print("4,update fee")
        print("5,delete fee")
        print("6,Exit")
        
        choice=input("enter choice(1-6):")
        
        if choice=="1":
            add_fee()
            
        elif choice=="2":
            show_fee()
            
        elif choice=="3":
            search_fee()
            
        elif choice=="4":
            update_fee()
            
        elif choice=="5":
            delete_fee()
            
        elif choice=="6":
            break
        
def load_fees():
    try:
        file=open("fees.json","r")
        fees=json.load(file)
        file.close()
        return fees
    except:
        return[]
def save_fees(fees):
    file=open("fees.json","w")
    json.dump(fees,file,indent=4)
    file.close
    
def add_fee():
    fees=load_fees()
    student_id=input("enter student id:")
    month=input("enter your require month:")
    amount=input("enter your require amount:")
    status=input("enter your status:")
        
    new_fees={
        "student_id":student_id,
        "month":month,
        "amount":amount,
        "status":status
    }
    fees.append(new_fees)
    save_fees(fees)
    print("fees added successfully.")
    
def show_fee():
    fees=load_fees()
    if len(fees)==0:
        print("no fee found.")
        return
    print("_"*50)
    print(f"{'student_id':<15}{'month':<15}{'amount':<10}{'status':<10}")
    print("_"*50)
    for fee in fees:
        print(f"{fee['student_id']:<15}{fee['month']:<15}{fee['amount']:<10}{fee['status']:<10}")
        print("_"*50)
    
def search_fee():
    
    fees=load_fees()
    student_id=input("enter student id:")
    month=input("enter month:")
    
    found=False
    
    for fee in fees:
        if fee["student_id"]==student_id and fee["month"]==month:
            
            print("----------------------------------------")
            print("student_id:",fee["student_id"])
            print("month:",fee["month"])
            print("amount:",fee["amount"])
            print("status:",fee["status"])
            found=True
            break
        if not found:
            print("fee not found.")
    
def update_fee():
    fees=load_fees()
    student_id=input("enter student_id:")
    month=input("enter month")
    found=False
    for fee in fees:
        if fee["student_id"]==student_id and fee["month"]==month:
            print("--------------------------------------")
            fee["amount"]=int(input("enter new amount:"))
            fee["status"]=input("enter new status:")
            save_fees(fees)
            print("fee update successfully.")
            found=True
            break
    if not found:
        print("fee not found.")
def delete_fee():
    fees=load_fees()
    student_id=input("enter student id:")
    month=input("enter month:")
    found=False
    for fee in fees:
        if fee["student_id"]==student_id and fee["month"]==month:
            print("student_id and month found.")
            print("amount:",fee["amount"])
            print("statue:",fee["status"])
            confirm=input("Are you sure?(y/n):")
            if confirm.lower()=="y":
                fees.remove(fee)
                save_fees(fees)
                print("fee delete successfully.")
                found=True
                break
            if not found:
                print("fee not found.")