a=int(input("english marks"))
b=int(input("python marks"))
c=int(input("mwe marks"))
avg=(a+b+c)//3
print(avg)
if avg==80:
     print("A+")
elif avg>60 and  avg<80:
    print("B")
else:
     print("pass")
