item=input("Enter item: ")
price=float(input("Enter price: "))
ons=int(input("Overnight delivery(0=no,1=yes) "))
print("Invoice:")
if price<10:
    print(item,price,sep="  ")
    if ons==1:
        sc=2+5
    else:
        sc=2
    print("Shipping  ",sc)
    tot=price+sc
    print("Total  ",tot)
elif price>=10:
    print(item,price,sep="  ")
    if ons==1:
        sc=2+5
    else:
        sc=2
    print("Shipping  ",sc)
    tot=price+sc
    print("Total  ",tot)