#Nested if - else example
a=int(input("Enter the valur of a :"))
b=int(input("Enter the valur of b :"))
c=int(input("Enter the valur of c :"))

if a>b:
    if a>c:
        print("a is gratest")
    else:
        print("c ia gretest")

else:
    if b>c:
        print("b is gretest")
    else:
        print("c is gretest")    