mytuple=("naveen","sudheer","sumanth","surya",)
print(mytuple)
print(type(mytuple))
mytuple=mytuple+("hello",)
mytuple[1]=("sudheer")
mytuple=mytuple+(14,23,"joe")
print(mytuple)
for i in range(0,5):
    n=int(input("enter"))
    mytuple=mytuple+(n,)
