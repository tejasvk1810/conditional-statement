#Calculations with user choice

no1=int(input("Enter the no :"))
no2=int(input("Enyter the no :"))
print("1.add\n2.sub\n3.mult\n4.div")

ch=int(input("Enter the choice :"))
if(ch==1):
    ans=no1+no2
    print("sum :",ans)
elif(ch==2):
    ans=no1-no2
    print("sub :",ans)
elif(ch==3):
    ans=no1*no2
    print("mult :",ans)
elif(ch==4):
    ans=no1/no2
    print("div :",ans)
else:
    print("invalid choice")    
    

