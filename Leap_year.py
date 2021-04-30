year=2004
year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("2004 leap year")
        else:           
            print("not leap year")
    else:
        print("it is leap year")
else:
    print("not leap year")