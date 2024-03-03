#MARKSHEET EXAMPLE
name=str(input("Enter the name :"))
rollno=int(input("Enter the rollno :"))
math=int(input("Enter the marks of mathematics :"))
eng=int(input("Enter the marks of english :"))
sci=int(input("Enter the marks of science :"))

total=(math+eng+sci)
per=float(total/3)

print("name :",name)
print("rollno :",rollno)
print("math :",math)
print("eng :",eng)
print("sci :",sci)
print("total :",total)
print("percentage :",per)

if(per>=0 and per<40):
    print("Grade D")
elif(per>=40 and per<55):
    print("Grade C")
elif(per>=55 and per<70):
    print("Grade B")
elif(per<=70 and per<85):
    print("Grade A")
elif(per>=85 and per<100):
    print("Grade A+")
else:
    print("something went wrong")
            
