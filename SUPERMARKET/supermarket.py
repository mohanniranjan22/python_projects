#-----------------------------SUPER MARKET BILL GENERATION-------------------------------
from datetime import datetime 
d={"rice":50,"sugar":30,"oil":110,"salt":20,"boost":300,"biscuts":30,"chocolates":50,"cooldrink":90,"surf":50,"soaps":50}
d_k=[]
for i in d:
    d_k.append(i) #items names  appending into list
print("-----------------------------SUPER MARKET BILL GENERATION-------------------------------")
s='''
1.Rice RS 50 per kg
2.Sugar RS 30 per kg
3.oil RS 110 per litre
4.salt RS 20 per kg
5.boost RS 300 per kg
6.biscuts RS 30 per packet
7.chocolates RS 50 per packet
8.cooldrink RS 90 per litre
9.surf RS 50 per kg
10.soaps RS 50 per pack
'''
heading_cloumn=["S.NO","ITEMS","QUANTITY","PRICE"]
d1={} #items and quantity stores in this dictionary
print(s) #printing available items
while True: #this bill continue until you press control+c because so many users comes so our program runs contiue until market closed
    b=input("if you want to buy enter y/Y for no enter n/N:")
    if(b=="n" or b=="N"):#if no again ask b that is above statement
        continue
    if(b=="y" or b=="Y"):
     while True:
        name=input("Enter your name:")
        while True:#loop for no of items want to buy
            item=input("Enter the item name:")
            quantity=int(input("Enter the how much Quantity of item you want:"))
            if(item in d_k):#checking whether customer wants item is in our items list or not 
              d1[item]=quantity
              option1=input("if you want to buy another item enter y/n:")
              if(option1=="n"):
                 break
              if(option1=="y"):
                 continue
            else: #if you entered wrong item it will exicute
                print("item not present choose correct item from displaing items:")
                continue #again ask enter item
        n=input("can i bill this items enter y/n:")
        if(n=="n"):
            continue#again it will ask items to buy
        if(n=="y"):
            total_price=0
            for i in d1:
                if(i in d):
                 total_price+=(d1.get(i)*d.get(i))
            gst_amount=total_price*(15/100)
            final_amount=gst_amount+total_price
            print("="*44,"ram supermarket","="*44)
            print(" "*48,"ongole"," "*48)
            print("name:",name," "*60,"date:",datetime.now())
            print("-"*105)
            for i in heading_cloumn: #printing headings
                print(i,end=" "*15)
            print("\n")
            k=0
            for i in d1:
                k+=1
                k1=len(i)
                if(k//10!=0):
                    c=2
                else:
                    c=1
                c1=str(d1.get(i))
                c2=len(c1)
    
                print(k," "*(18-c),i," "*(17-k1),d1.get(i)," "*(21-c2),(d1.get(i)*d.get(i)))
            print("-"*105)
            print(" "*75,"totalamount : Rs ",total_price)
            print("gst amount"," "*69,"gst Rs : ",gst_amount)
            print("-"*105)
            print(" "*75,"finalamount : Rs ",final_amount)
            print("-"*105)
            print(" "*42,"thanks for visting"," "*42)
            print("-"*105)
            break










            

            




            




