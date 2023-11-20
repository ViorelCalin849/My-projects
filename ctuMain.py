class ctuStock:
    def __init__(self, shop_name, shop_location, customers, sales, returns):
        self.shop_name = shop_name
        self.shop_location = shop_location
        self.customers = customers
        self.sales = sales
        self.returns = returns

# Creating four ctuStock objects with default values
shop1 = ctuStock("Default", "Default", 0, 0, 0)
shop2 = ctuStock("Default", "Default", 0, 0, 0)
shop3 = ctuStock("Default", "Default", 0, 0, 0)
shop4 = ctuStock("Default", "Default", 0, 0, 0)

#Making lists
Stock_Name_List1 = []
Stock_Amount_List1 = []
Stock_Price_List1 = []

Stock_Name_List2 = []
Stock_Amount_List2 = []
Stock_Price_List2 = []

Stock_Name_List3 = []
Stock_Amount_List3 = []
Stock_Price_List3 = []

Stock_Name_List4 = []
Stock_Amount_List4 = []
Stock_Price_List4 = []


#Creating of the Main Menu
def mainmenu():
    print(f"\nWelcome to CTU Technologies\n")
    print(" 1. Shop management \n 2. Sales \n 3. Returns \n 4. Stock \n 99. Exit \n")
    options = ["1","2","3","4","99"]
    while True:
        user_input= input("Select an option or 99 to exit: ")
        if user_input not in options:
            print("\nSorry that is not a valid option try again")
        if user_input in options:
            if user_input == "1":
                Shop_Managment()
            elif user_input == "2":
                Sales()
            elif user_input == "3":
                returns()
            elif user_input == "4":
                Stock()
            elif user_input == "99":
                break
                

#Creating Shop management menu
def Shop_Managment():
    print(f"Shop management\n1. Change shop Name\n2. Change shop location\n3. Display current shops\n4. Display all shops information\n0. Back" )
    options = ["1","2","3","4","0"]
    while True:
        user_input = input("\nSelect an option: ")
        if user_input not in options:
            print("\nSorry that is not a valid option try again")
        if user_input in options:
            if user_input == "1":
                Change_Name()
            elif user_input == "2":
                Change_Location()
            elif user_input == "3":
                Display_Shops()
            elif user_input == "4":
                All_info()
            elif user_input == "0":
                mainmenu()

#Change Shop Name menu
def Change_Name():
    while True:
        print("Change Shop Name \n\n Select Shop\n","1.",shop1.shop_name,"\n","2.",shop2.shop_name,"\n","3.",shop3.shop_name,"\n","4.",shop4.shop_name,"\n 0. Back")
        options = ["1","2","3","4","0"]
        user_input = input("Select an option: ")
        if user_input in options:
            if user_input == "1":
                Name_Change = input("Type the new Shop name: ")
                if Name_Change == "":
                    print("\nSorry that is not a valid name try again.")
                else:
                    shop1.shop_name = Name_Change
                    print("\nShop name was successfully changed to",shop1.shop_name)
            elif user_input == "2":
                Name_Change = input("Type the new Shop name: ")
                if Name_Change == "":
                    print("\nSorry that is not a valid name try again.")
                else:
                    shop2.shop_name = Name_Change
                    print("\nShop name was successfully changed to",shop2.shop_name)      
            elif user_input == "3":
                Name_Change = input("Type the new Shop name: ")
                if Name_Change == "":
                    print("\nSorry that is not a valid name try again.")
                else:
                    shop3.shop_name = Name_Change
                    print("\nShop name was successfully changed to",shop3.shop_name)  
            elif user_input == "4":
                Name_Change = input("Type the new Shop name: ")
                if Name_Change == "":
                    print("\nSorry that is not a valid name try again.")
                else:
                    shop4.shop_name = Name_Change
                    print("\nShop name was successfully changed to",shop4.shop_name)
            if user_input == "0":
                Shop_Managment()


#Change Shop Location
Location_options = ['Free State','KZN', 'Limpopo','Gauteng']
def Change_Location():
    while True:
        print("Change Shop Location\n\nSelect shop\n1.",shop1.shop_name+',',shop1.shop_location,"\n2.",shop2.shop_name+',',shop2.shop_location,"\n3.",shop3.shop_name+',',shop3.shop_location,"\n4.",shop4.shop_name+',',shop4.shop_location,"\n0. Back")
        options = ["1","2","3","4","0"]
        user_input = input("Select an option: ")
        if user_input in options:
            if user_input == "1":
                try:
                    Location_change1 = input("Enter a location Free State, Gauteng, KZN, Limpopo: ")
                except ValueError:
                    print("Invalid option or location has been misspelt.\nTry again using correct upper/lower case letters.\n ")
                    continue
                if Location_change1 not in Location_options:
                    print("Invalid option")
                    continue
                shop1.shop_location = Location_change1
                print("\nShop location was successfully changed to",shop1.shop_location)
            elif user_input == "2":
                try:
                    Location_change2 = input("Enter a location Free State, Gauteng, KZN, Limpopo: ")
                except ValueError:
                    print("Invalid option or location has been misspelt.\nTry again using correct upper/lower case letters.\n ")
                    continue
                if Location_change2 not in Location_options:
                    print("Invalid option")
                    continue
                shop2.shop_location = Location_change2
                print("\nShop location was successfully changed to",shop2.shop_location)     
            elif user_input == "3":
                try:
                    Location_change3 = input("Enter a location Free State, Gauteng, KZN, Limpopo: ")
                except ValueError:
                    print("Invalid option or location has been misspelt.\nTry again using correct upper/lower case letters.\n ")
                    continue
                if Location_change3 not in Location_options:
                    print("Invalid option")
                    continue
                shop3.shop_location = Location_change3
                print("\nShop location was successfully changed to",shop3.shop_location)  
            elif user_input == "4":
                try:
                    Location_change4 = input("Enter a location Free State, Gauteng, KZN, Limpopo: ")
                except ValueError:
                    print("Invalid option or location has been misspelt.\nTry again using correct upper/lower case letters.\n ")
                    continue
                if Location_change4 not in Location_options:
                    print("Invalid option")
                    continue
                shop4.shop_location = Location_change4
                print("\nShop location was successfully changed to",shop4.shop_location)
            if user_input == "0":
                Shop_Managment()
        
def Display_Shops():
    print("Current Shops","\n\n1. ",shop1.shop_name+',',shop1.shop_location,"\n2. ",shop2.shop_name+',',shop2.shop_location,"\n3. ",shop3.shop_name+',',shop3.shop_location,"\n4. ",shop4.shop_name+',',shop4.shop_location)
    print()
    Shop_Managment()

def All_info():
    print("----------------\nShop Name:",shop1.shop_name,"\nShop Location:",shop1.shop_location,"\nNumber of customers:",shop1.customers,"\nCurrent Sales",shop1.sales,"\nReturns:",shop1.returns,"\n----------------")
    print("----------------\nShop Name:",shop2.shop_name,"\nShop Location:",shop2.shop_location,"\nNumber of customers:",shop2.customers,"\nCurrent Sales",shop2.sales,"\nReturns:",shop2.returns,"\n----------------")
    print("----------------\nShop Name:",shop3.shop_name,"\nShop Location:",shop3.shop_location,"\nNumber of customers:",shop3.customers,"\nCurrent Sales",shop3.sales,"\nReturns:",shop3.returns,"\n----------------")
    print("----------------\nShop Name:",shop4.shop_name,"\nShop Location:",shop4.shop_location,"\nNumber of customers:",shop4.customers,"\nCurrent Sales",shop4.sales,"\nReturns:",shop4.returns,"\n----------------")
    Shop_Managment()

# Sales Menu
def Sales():
    while True:
        print("\nStores to purchase stock from:\n1. ",shop1.shop_name,"\n2. ",shop2.shop_name,"\n3. ",shop3.shop_name,"\n4. ",shop4.shop_name,"\n0.  Back")
        options = ["1","2","3","4","0"]
        user_input = input("What store would you like to purchase from: ")
        if user_input in options:
            if user_input == "1":
                #creating output for no availiable stock
                if not Stock_Amount_List1:                                                                                         
                    print("\nNo stock available to display.\nGo to the stock menu to add more.")
                else: #Print out for when there is stock
                    for i in range(len(Stock_Name_List1)):
                        print(f"{i+1}. {Stock_Name_List1[i]}, Price: {Stock_Price_List1[i]}, Quantity: {Stock_Amount_List1[i]}")
                    #print(f"Stock name             : {Stock_Name_List1}.\nStock price in Rands   : {Stock_Price_List1}.\nStock quantity per unit: {Stock_Amount_List1}.\n")
                    try:   
                        item = int(input("\nWhat would you like to purchase or enter 0 to go back: "))
                    except:
                        print("Invalid option")

                    if item == 0:
                        mainmenu()
                    else:
                        while True:
                            try:
                                Quantity = int(input("How many would you like to purchase?: "))
                            except:
                                print("Not a valid option")
                                Sales()
                            print(f"Your Total is: R{Quantity*Stock_Price_List1[item-1]}")
                            choice = input("\nPress Y/N to to confirm your order\n").upper()
                            options = ["Y","N"]
                            if choice not in options:
                                print("Invalid option: Try again")
                            elif choice == "N":
                                mainmenu()
                            else:
                                if choice in options:
                                    if choice == "Y":
                                        print("Your product has succefully been bought")
                                        shop1.customers += 1
                                        shop1.sales += Quantity
                                        Stock_Amount_List1[item-1] -= Quantity

                            break

            if user_input == "2":
                #creating output for no availiable stock
                if not Stock_Amount_List2:                                                                                         
                    print("\nNo stock available to display.\nGo to the stock menu to add more.")
                else: #Print out for when there is stock
                    for i in range(len(Stock_Name_List2)):
                        print(f"{i+1}. {Stock_Name_List2[i]}, Price: {Stock_Price_List2[i]}, Quantity: {Stock_Amount_List2[i]}")
                    try:   
                        item = int(input("\nWhat would you like to purchase or enter 0 to go back: "))
                    except:
                        print("Invalid option")

                    if item == 0:
                        mainmenu()
                    else:
                        while True:
                            try:
                                Quantity = int(input("How many would you like to purchase?: "))
                            except:
                                print("Not a valid option")
                                Sales()
                            print(f"Your Total is: R{Quantity*Stock_Price_List2[item-1]}")
                            choice = input("\nPress Y/N to to confirm your order\n").upper()
                            options = ["Y","N"]
                            if choice not in options:
                                print("Invalid option: Try again")
                            elif choice == "N":
                                mainmenu()
                            else:
                                if choice in options:
                                    if choice == "Y":
                                        print("Your product has succefully been bought")
                                        shop2.customers += 1
                                        shop2.sales += Quantity
                                        Stock_Amount_List2[item-1] -= Quantity

                            break

            if user_input == "3":
                #creating output for no availiable stock
                if not Stock_Amount_List3:                                                                                         
                    print("\nNo stock available to display.\nGo to the stock menu to add more.")
                else: #Print out for when there is stock
                    for i in range(len(Stock_Name_List3)):
                        print(f"{i+1}. {Stock_Name_List3[i]}, Price: {Stock_Price_List3[i]}, Quantity: {Stock_Amount_List3[i]}")
                    try:   
                        item = int(input("\nWhat would you like to purchase or enter 0 to go back: "))
                    except:
                        print("Invalid option")

                    if item == 0:
                        mainmenu()
                    else:
                        while True:
                            try:
                                Quantity = int(input("How many would you like to purchase?: "))
                            except:
                                print("Not a valid option")
                                Sales()
                            print(f"Your Total is: R{Quantity*Stock_Price_List3[item-1]}")
                            choice = input("\nPress Y/N to to confirm your order\n").upper()
                            options = ["Y","N"]
                            if choice not in options:
                                print("Invalid option: Try again")
                            elif choice == "N":
                                mainmenu()
                            else:
                                if choice in options:
                                    if choice == "Y":
                                        print("Your product has succefully been bought")
                                        shop3.customers += 1
                                        shop3.sales += Quantity
                                        Stock_Amount_List3[item-1] -= Quantity

                            break             

            if user_input == "4":
                #creating output for no availiable stock
                if not Stock_Amount_List4:                                                                                         
                    print("\nNo stock available to display.\nGo to the stock menu to add more.")
                else: #Print out for when there is stock
                    for i in range(len(Stock_Name_List4)):
                        print(f"{i+1}. {Stock_Name_List4[i]}, Price: {Stock_Price_List4[i]}, Quantity: {Stock_Amount_List4[i]}")
                    try:   
                        item = int(input("\nWhat would you like to purchase or enter 0 to go back: "))
                    except:
                        print("Invalid option")

                    if item == 0:
                        mainmenu()
                    else:
                        while True:
                            try:
                                Quantity = int(input("How many would you like to purchase?: "))
                            except:
                                print("Not a valid option")
                                Sales()
                            print(f"Your Total is: R{Quantity*Stock_Price_List4[item-1]}")
                            choice = input("\nPress Y/N to to confirm your order\n").upper()
                            options = ["Y","N"]
                            if choice not in options:
                                print("Invalid option: Try again")
                            elif choice == "N":
                                mainmenu()
                            else:
                                if choice in options:
                                    if choice == "Y":
                                        print("Your product has succefully been bought")
                                        shop4.customers += 1
                                        shop4.sales += Quantity
                                        Stock_Amount_List4[item-1] -= Quantity

                            break                            
            if user_input == "0":
                mainmenu()

# Stock Menu
def Stock():
    while True:
        print("\nShop Stocks\n1. Display Stock\n2. Add Stock\n0. Back")
        options = ["1","2","3","4","0"]
        user_input = input("Select an option: ")
        if user_input in options:
            if user_input == "1":
                 Display_stock()
            if user_input == "2":
                Add_Stock()
            if user_input == "0":
                mainmenu()

#Displaying the stock menu
def Display_stock():
    while True:
        print("\nWhich stores stocks would you like to see?\n","1.",shop1.shop_name,"\n","2.",shop2.shop_name,"\n","3.",shop3.shop_name,"\n","4.",shop4.shop_name,"\n 0. Back")
        options = ["1","2","3","4","0"]
        user_input = input("Select an option: ")
        if user_input in options:
                if user_input == "1":
                    if not Stock_Amount_List1:                                                                                         
                        input("\nNo stock available to display.\nGo to the stock menu to add more.\n\npress anything to go back: ")
                    else:
                        print("\n",shop1.shop_name)
                        for i in range(len(Stock_Name_List1)):
                            print(f"{i+1}. {Stock_Name_List1[i]}, Price: R{Stock_Price_List1[i]}, Quantity: {Stock_Amount_List1[i]}")
                if user_input == "2":
                    if not Stock_Amount_List1:                                                                                         
                        input("\nNo stock available to display.\nGo to the stock menu to add more.\n\npress anything to go back: ")
                    else:
                        print("\n",shop2.shop_name)
                        for i in range(len(Stock_Name_List2)):
                            print(f"{i+1}. {Stock_Name_List2[i]}, Price: R{Stock_Price_List2[i]}, Quantity: {Stock_Amount_List2[i]}")
                if user_input == "3":
                    if not Stock_Amount_List3:                                                                                         
                        input("\nNo stock available to display.\nGo to the stock menu to add more.\n\npress anything to go back: ")
                    else:
                        print("\n",shop3.shop_name)
                        for i in range(len(Stock_Name_List3)):
                            print(f"{i+1}. {Stock_Name_List3[i]}, Price: R{Stock_Price_List3[i]}, Quantity: {Stock_Amount_List3[i]}")
                if user_input == "4":
                    if not Stock_Amount_List4:                                                                                         
                        input("\nNo stock available to display.\nGo to the stock menu to add more.\n\npress anything to go back: ")
                    else:
                        print("\n",shop4.shop_name)
                        for i in range(len(Stock_Name_List4)):
                            print(f"{i+1}. {Stock_Name_List4[i]}, Price: R{Stock_Price_List4[i]}, Quantity: {Stock_Amount_List4[i]}")
                if user_input == "0":
                    Stock()

#Adding to our stock menu
def Add_Stock():
    while True:
        print("\nWhich stores stocks would you like to increase?\n","1.",shop1.shop_name,"\n","2.",shop2.shop_name,"\n","3.",shop3.shop_name,"\n","4.",shop4.shop_name,"\n 0. Back")
        options = ["1","2","3","4","0"]
        #What store to add stock to
        user_input = input("Select a store to add stock to: ")
        if user_input in options:
            if user_input == "1":
                name = input("Enter name of the new stock: ")
                Stock_Name_List1.append(name)
                while True:
                    try:
                        ammount = int(input("Quantity of new stock: "))
                    except ValueError:
                        print("Invalid: Try again")
                        continue
                    break
                Stock_Amount_List1.append(ammount)
                while True:
                    try:
                        price = int(input("Price of your stock: "))
                    except ValueError:
                        print("Invalid: Try again")
                        continue
                    break
                Stock_Price_List1.append(price)

            elif user_input == "2":
                name = input("Enter name of the new stock: ")
                Stock_Name_List2.append(name)
                while True:
                    try:
                        ammount = int(input("Quantity of new stock: "))
                    except ValueError:
                        print("Invalid: Try again")
                        continue
                    break
                Stock_Amount_List2.append(ammount)
                while True:
                    try:
                        price = int(input("Price of your stock: "))
                    except ValueError:
                        print("Invalid: Try again")
                        continue
                    break
                Stock_Price_List2.append(price)

            elif user_input == "3":
                name = input("Enter name of the new stock: ")
                Stock_Name_List3.append(name)
                while True:
                    try:
                        ammount = int(input("Quantity of new stock: "))
                    except ValueError:
                        print("Invalid: Try again")
                        continue
                    break
                Stock_Amount_List3.append(ammount)
                while True:
                    try:
                        price = int(input("Price of your stock: "))
                    except ValueError:
                        print("Invalid: Try again")
                        continue
                    break
                Stock_Price_List3.append(price)

            elif user_input == "4":
                name = input("Enter name of the new stock: ")
                Stock_Name_List4.append(name)
                while True:
                    try:
                        ammount = int(input("Quantity of new stock: "))
                    except ValueError:
                        print("Invalid: Try again")
                        continue
                    break
                Stock_Amount_List4.append(ammount)
                while True:
                    try:
                        price = int(input("Price of your stock: "))
                    except ValueError:
                        print("Invalid: Try again")
                    break
                Stock_Price_List4.append(price)
            elif user_input == "0":
                Stock()

#Creating the returns menu
def returns():
    while True:
        print("\nStores to return stock to:\n1. ",shop1.shop_name,"\n2. ",shop2.shop_name,"\n3. ",shop3.shop_name,"\n4. ",shop4.shop_name,"\n0.  Back")
        options = ["1","2","3","4","0"]
        user_input = input("\nWhat store would you like to return stock to: ")
        if user_input in options:
            if user_input == "1":
                #creating output for no availiable stock
                if not Stock_Amount_List1:                                                                                         
                    print("\nNo stock available to display.\nGo to the stock menu to add more.")
                else: #Print out for when there is stock
                    print("\n"+shop1.shop_name)
                    for i in range(len(Stock_Name_List1)):
                        print(f"\n{i+1}. Stock: {Stock_Name_List1[i]}, Price: {Stock_Price_List1[i]}, Quantity: {Stock_Amount_List1[i]}")
                    try:   
                        item = int(input("\nWhat stock option would you like to return? or enter 0 to go back: "))
                    except:
                        print("Invalid option")

                    if item == 0:
                        mainmenu()
                    else:
                        while True:
                            try:
                                Quantity = int(input("How many would you like to return?: "))
                            except:
                                print("Not a valid option")
                                Sales()
                            print(f"Your Total is: R{Quantity*Stock_Price_List1[item-1]}")
                            choice = input("\nPress Y/N to to confirm your return order\n").upper()
                            options = ["Y","N"]
                            if choice not in options:
                                print("Invalid option: Try again")
                            elif choice == "N":
                                mainmenu()
                            else:
                                if choice in options:
                                    if choice == "Y":
                                        print("Your product has succefully been returned")
                                        shop1.sales -= Quantity
                                        Stock_Amount_List1[item-1] += Quantity

                            break

            if user_input == "2":
                #creating output for no availiable stock
                if not Stock_Amount_List2:                                                                                         
                    print("\nNo stock available to display.\nGo to the stock menu to add more.")
                else: #Print out for when there is stock
                    print("\n"+shop2.shop_name)
                    for i in range(len(Stock_Name_List2)):
                        print(f"\n{i+1}. {Stock_Name_List2[i]}, Price: {Stock_Price_List2[i]}, Quantity: {Stock_Amount_List2[i]}")
                    try:   
                        item = int(input("\nWhat store would you like to return stock to or enter 0 to go back: "))
                    except:
                        print("Invalid option")

                    if item == 0:
                        mainmenu()
                    else:
                        while True:
                            try:
                                Quantity = int(input("How many would you like to return?: "))
                            except:
                                print("Not a valid option")
                                Sales()
                            print(f"Your Total is: R{Quantity*Stock_Price_List2[item-1]}")
                            choice = input("\nPress Y/N to to confirm your return order\n").upper()
                            options = ["Y","N"]
                            if choice not in options:
                                print("Invalid option: Try again")
                            elif choice == "N":
                                mainmenu()
                            else:
                                if choice in options:
                                    if choice == "Y":
                                        print("Your product has succefully been returned")
                                        shop2.sales -= Quantity
                                        Stock_Amount_List2[item-1] += Quantity

                            break

            if user_input == "3":
                #creating output for no availiable stock
                if not Stock_Amount_List3:                                                                                         
                    print("\nNo stock available to display.\nGo to the stock menu to add more.")
                else: #Print out for when there is stock
                    print("\n"+shop3.shop_name)
                    for i in range(len(Stock_Name_List3)):
                        print(f"\n{i+1}. {Stock_Name_List3[i]}, Price: {Stock_Price_List3[i]}, Quantity: {Stock_Amount_List3[i]}")
                    try:   
                        item = int(input("\nWhat store would you like to return stock to or enter 0 to go back: "))
                    except:
                        print("Invalid option")

                    if item == 0:
                        mainmenu()
                    else:
                        while True:
                            try:
                                Quantity = int(input("How many would you like to return?: "))
                            except:
                                print("Not a valid option")
                                Sales()
                            print(f"Your Total is: R{Quantity*Stock_Price_List3[item-1]}")
                            choice = input("\nPress Y/N to to confirm your return order\n").upper()
                            options = ["Y","N"]
                            if choice not in options:
                                print("Invalid option: Try again")
                            elif choice == "N":
                                mainmenu()
                            else:
                                if choice in options:
                                    if choice == "Y":
                                        print("Your product has succefully been returned")
                                        shop3.sales -= Quantity
                                        Stock_Amount_List3[item-1] += Quantity

                            break             

            if user_input == "4":
                #creating output for no availiable stock
                if not Stock_Amount_List4:                                                                                         
                    print("\nNo stock available to display.\nGo to the stock menu to add more.")
                else: #Print out for when there is stock
                    print("\n"+shop4.shop_name)
                    for i in range(len(Stock_Name_List4)):
                        print(f"\n{i+1}. {Stock_Name_List4[i]}, Price: {Stock_Price_List4[i]}, Quantity: {Stock_Amount_List4[i]}")
                    try:   
                        item = int(input("\nwhat would you like to purchase or enter 0 to go back: "))
                    except:
                        print("Invalid option")

                    if item == 0:
                        mainmenu()
                    else:
                        while True:
                            try:
                                Quantity = int(input("How many would you like to purchase?: "))
                            except:
                                print("Not a valid option")
                                Sales()
                            print(f"Your Total is: R{Quantity*Stock_Price_List4[item-1]}")
                            choice = input("\nPress Y/N to to confirm your order\n").upper()
                            options = ["Y","N"]
                            if choice not in options:
                                print("Invalid option: Try again")
                            elif choice == "N":
                                mainmenu()
                            else:
                                if choice in options:
                                    if choice == "Y":
                                        print("Your product has succefully been returned")
                                        shop1.sales -= Quantity
                                        Stock_Amount_List1[item-1] += Quantity

                            break                            
            if user_input == "0":
                mainmenu()

mainmenu()