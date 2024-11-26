# registration and login programme

username = "prisca"
password = "xom15"
users=[]

def addnewregistration(firstname,lastname,email,state):
    new={}
    new["firstname"] = firstname
    new["lastname"] = lastname
    new["email"] = email
    new["state"] = state
    users.append(new)

while True:
     permission = int(input("please enter task to peform 1: for new registration 2:for login: 3: for result "))
     if permission == 1:
            firstname = input("please enter firstname: ")
            lastname = input("please enter lastname: ")
            address = input("please enter address: ")
            phone = input("please enter phone: ")
            email = input("please enter email:  ")
            state = input("please enter state:  ")
            addnewregistration(firstname,lastname,email,state)
     elif permission == 2 :
          newuser  = input("Enter new username:")
          newpass = input("Enter new password: ")
          if(username==newuser) and (password == newpass):
                print("sucessful")
          else: 
               print("invalid username and password")
          print(users)  
       
           


    