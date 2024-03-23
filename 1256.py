n=24
sum=0
for i in range(1,n):
    if n%i==0:
        sum =sum+2
        if sum>n:
            print("sum of factors greaterthan a")
        else:
                print("sum of factors not greaterthan a")
