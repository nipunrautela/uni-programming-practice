def rec(a,b):
    if a==b:
        return a
    else:
        if a>b:
            rec(min(a,b),b)
        else:
            rec(a,min(a,b))
a=int(input("Enter no. of Chocolates of type 1 : "))
b=int(input("Enter no. of Chocolates of type 2 : "))
print(rec(a,b))