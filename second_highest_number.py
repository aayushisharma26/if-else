a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b<c:
    print("a is second highest number")
elif a<b>c:
    print("a is second highest number")
elif a>b<c:
    print("b is second highest number")
elif a<b>c:
    print("b is second highest number")
elif a<b<c:
    print("c is second highest number")
elif a>b>c:
    print("c is second highest number")
else:
    print("invailid number")