a={}

size=int(input("enter the range:"))
for i in range(0,size):
     x=input("enter the key:")
     y=input("enter the value:")
     a.update({x:y})
print(a)