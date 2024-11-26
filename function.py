p = 6000
r = 0.5
t = 2

def simple_interset():
    si = (p*r*t)/100
    print(si)

def loginauth(userinput, username, password, passinput):
    if userinput == username and passinput == password:
        print("login successful")
    else:
        print("invalid login or password")

users = ["afrimagic", "chiwawa"]
userspass = ["123456", "1234"]

while True:
    userinput = input("please enter username: ")
    passinput = input("please enter user password: ")
    for item in users: 
        if item == userinput: 
            username = item
            break
        else:
            username = "null"
    for item2 in userspass: 
        if item2 == passinput: 
            password = item2
            break
        else:
            password = "null"
            loginauth(userinput, username, password, passinput)
            break
        


