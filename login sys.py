def login():
    n = 1 
    while n!=0:
        uname = input("enter username")
        pwd = input("enter password")
        if uname==pwd:
            print("login sucessfull")
            break
        else:
            print("invalid enter again")
