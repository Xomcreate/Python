# display biodata
biodata= []
for Q in range(1,7):
    # firstname,lastname, address, phone, email, state, country
    if Q == 1:
        data = input("please enter your firstname: ")
        biodata.append(data)
       
    if Q == 2:
        data = input("please enter your lastname: ")
        biodata.append(data)
      
    if Q == 3:
        data = input("please enter your address: ")
        biodata.append(data)
       
    if Q == 4:
        data = input("please enter your phone: ")
        biodata.append(data)
       
    if Q == 5:
        data = input("please enter your email: ")
        biodata.append(data)
       
    if Q == 6:
        data = input("please enter your state: ")
        biodata.append(data)
      
    if Q == 7:
        data = input("please enter your country: ")
        biodata.append(data)
        
print(biodata)

