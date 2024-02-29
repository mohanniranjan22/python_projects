
print("="*20)
customers_list=['lesh','charan','nasir','vignesh','suresh']
customer_names_balnaces={'lesh':10000,'charan':20000,'nasir':15000,'vignesh':12000,'suresh':11000}
customer_names_pins={'lesh':'1234','charan':'4321','nasir':'1235','vignesh':'1245','suresh':'1123'}

# This statement below helps the program to run continuously.
i=1
while True:
    print("=====================================")
    print(" ----Welcome to Times Bank----       ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance  >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*************************************")

    # The below statement takes the choice number from the user.
    choice=int(input("Enter your choice from the above menu : "))
    if(choice==1):
        print("choice 1 is selected by customer")
        # The line below will take the no:of customers from the user.
        no_of_customers = int(input("Number of Customers : "))
        if no_of_customers>5:
            while True:
            # The if condition will restrict the number of new account to 5.
                if(no_of_customers>5):           
                    print("\n")
                    print("Customer registration exceed reached or Customer registration too low")
                    k=int(input("Number of Customer : "))
                    no_of_customers=k
                    continue
                else:
                    break
        else:
            # The while loop will run according to the no:of customers.
            while i<=no_of_customers:
              i1=3
            
              while i1!=0:
                balance=0
                name=input("Please enter your full name:")
                pin=input("Please enter your pin that is your choice :")
                if ((name or pin)  not in customer_names_pins ):
                    customer_names_pins.update({name:pin})
                    customers_list.append(name)
                    
                    deposition=int(input("please deposit 500 Rs/- to start an account"))
                    if deposition<500:
                        while True:
                            print("please deposit 500 Rs /-")

                            if deposition < 500:
                                k1=int(input("please deposit 500 Rs/- to start an account"))
                                deposition=k1
                                continue
                            else:
                              break
                    else:
                        balance+=deposition
                        customer_names_balnaces.update({name:balance})
                        print("\nName=", end=" ")
                        print(name)
                        print("Pin=",end=" ")
                        print(pin)
                        print("Balance=", end=" ")
                        print(balance,"-/Rs")
                        print("\nYour name is added to customers system")
                        print("Your pin is added to customer system")
                        print("Your balance is added to customer system")
                        print("----New account created successfully !----")
                        print("\n")
                        print("Your name is avalilable on the customers list now : ")
                        print(customers_list)
                        print("\n")
                        print("Note! Please remember the Name and Pin")
                        print("========================================")
                        i+=1
                        break
                else:
                    print("name or pin already exist")
                    i-=1
        continue
    elif choice==2:
        print("Choice number 2 is selected by the customer")
            # This while loop will prevent the user using the account if the username or pin is wrong.
        while True:
            name=input("Enter your name:")
            pin=input("Enter your pin:")
            for j in customer_names_pins:
                if(name==j and pin==customer_names_pins[j]):
                    print("Your Current Balance:", end=" ")
                    print(customer_names_balnaces[j],"-/Rs")
                    balance=(customer_names_balnaces[j])
                    withdraw=int(input("Enter the amount you want to withdraw:"))
                    if(withdraw>balance):
                       while True:
                        if(withdraw>balance):
                            opt=input("your balance is low so you want to deopasit enter y/Y for exit n/N:")
                            if( opt=='y'):
                                deposit1=int(input("Enter amount for deposit because your balance is low:  "))
                                balance+=deposit1
                                break

                            else:
                                break
                    balance-=withdraw
                    customer_names_balnaces.update({j:balance})  
                    print("-\n")
                    print("----Withdraw Successfull!----") 
                    print("Your New Balance: ", balance, "-/Rs")
                    break
                else:
                    print('name or pin is inncorrect')
                    break    
                    
            break
        continue
    elif(choice==3):
        print("Choice number 3 is selected by the customer:")
        while True:
            name=input("Enter your name:")
            pin=input("Ennter your pin:")
            for j in customer_names_pins:
                if (name==j and pin==customer_names_pins[j]):
                    print("your balance is ",customer_names_balnaces[j],"-/Rs")
                    balance=customer_names_balnaces[j]
                    deposit1=int(input("Enter amount you want to deposit:"))
                    balance+=deposit1
                    customer_names_balnaces.update({j:balance})
                    print("\n")
                    print("----Deposition successful!----")
                    print("Your New Balance: ",balance,"-/Rs\n\n")
                    break

                else:
                    print("name or pin inncorrect")
                    continue
            break
        continue

    elif(choice==4):
        print("Choice 4 is selected by the customer")
        for j in customer_names_balnaces:
            print(j,customer_names_balnaces.get(j))
        print("="*20)
        name=input("Enter your name :")
        pin=input("Enter your pin:")
        for j in customer_names_pins:
            if(name==j and pin==customer_names_pins[j]):
                print("your name is : ",j)
                print("your balance is : ",customer_names_balnaces[j])
        continue
    elif choice==5:
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print("Bye bye")
        break
    else:
        print("Invalid option selected by the customer ")
        print("Please Try again!")
        continue
        
        

            
         
                        
            
    
                        















               




        