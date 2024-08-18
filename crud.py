import pandas as pd
df = pd.read_csv('data_csv')
print(df.to_string())
a = []
def Menu():
    print("1. Store in list")
    print("2. Remove from list")
    print("3. Update List")
    print("4. View List")
    a = input("Enter your option")
    return a
def StoreIntoList():
    name = input("Enter your name")
    password = input("Enter your password")
    role = input("Enter your role")
    MUser = (name,password,role)
    a.append(MUser)
    pd.Series(MUser)
def RemoveFromList():
    name = input("Enter the name you want to remove")
    password = input("Enter the password you want to remove")
    role = input("Enter the role")
    MUser = (name,password,role)
    if a.__contains__(MUser):
        a.remove(MUser)
    else:
          print("User not found")   
def ViewList():
    #for i in range (len(a)):
        print(a)    
def UpdateList():
    name = input("Enter the previous name")
    update = input("Enter updated name")

op = "0"
while op != "5":
    op = Menu()
    if op == "1":
             StoreIntoList()
    elif op == "2":
            RemoveFromList()
    elif op == "3":
            UpdateList()        
    elif op == "4":
            ViewList()            
    else:
            break       