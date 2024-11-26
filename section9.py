# book storage
book = []

# function to add new record to book

def addnewuser(firstname, lastname, address,phone,email):
    k = {}
    k["firstname"] = firstname
    k["lastname"] = lastname
    k["address"] = address
    k["phone"] = phone
    k["email"] = email
    book.append(k)


while True:
        action = int(input("please enter task to peform 1: for new user 2:for result: "))
        if action == 1:
            firstname = input("please enter firstname ")
            lastname = input("please enter lastname ")
            address = input("please enter address ")
            phone = input("please enter phone ")
            email = input("please enter email ")
            addnewuser(firstname, lastname, address,phone,email)
        else: 
            print(book)