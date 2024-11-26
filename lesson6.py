# to generate account number


phoneno  = (input("enter your phone number "))
accountno = "AC" + phoneno[-4:] + str(1234)

print("your account number is:", accountno )
