n=int(input("enter the number"))
temp=n
s=0
while n<0:
    rem=n%10
    s=s+(rem**3)
    n=n//10
  if temp==s:
      print("it is an original number")
else :
    print("it is not a original number")
