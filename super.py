n=153
nod=0
while n>0:
    n=n//10
    nod=nod+1
    n1=n
sum1=0
while n1>0:
    digit=n1%10
    sum1=sum1+digit**nod
    n1=n1//10
if  sum1==nod:
    print("it is original")
else:
    print("it is not original")

