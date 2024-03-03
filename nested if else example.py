# NESTED IF - ELSE EXAMPLE 2

print("1)CAR\n2)BIKE")
ch1=int(input("Enter your choice :"))

if(ch1==1):
    print("you selected Car Choice Now Further selected ")
    print("1.BMW\n2.AUDI\n3.HONDA\n4.FOURTUNER")

    ch2=int(input("Enter the choice for Car :"))
    if(ch2==1):
        print("you are selected car :BMW")
    elif(ch2==2):
        print("you are selected car : AUDI")
    elif(ch2==3):
        print("you are seletced car : HONDA")
    elif(ch2==4):
        print("you are selected car : FORTUNER")
    else:
        print("invalid selection of car")

elif(ch1==2):
     print("you selected Bike Choice Now Further selected ")
     print("1.KTM\n2.FZ\n3.MT15")

     ch3=int(input("Enter the choice for Car :"))
     if(ch3==1):
         print("you are selected bike : KTM")
     elif(ch3==2):
         print("you are selected bike : FZ")
     elif(ch3==3):
         print("you are selected bike : MT15")
     else:
         print("invalid selection")
else:
    print("invalid selection")                 
             
         



