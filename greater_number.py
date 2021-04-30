a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    print(a,"is greater number")
elif b>a and b>c:
    print(b,"is greater number")
elif c>a and c>b:
    print(c,"is greater number")    
else:
    print("it is not greater number")    