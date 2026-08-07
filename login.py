def login():
    users={
        "admin":{
            "password":"1234",
            "role":"Administrator"
        },
        "teacher":{
            "password":"abcd",
            "role":"teacher"
        },
        "student":{
            "password":"1111",
            "role":"student"
        }
        
    }
    username=input("user name:")
    password=input("password")
    
    if username in users:
        if users[username]["password"]==password:
            print("login successful")
            print("role",users[username]["role"])
            return True
        else:
            print("wrong password")
            return False
    else:
        print("user not found")
        return False