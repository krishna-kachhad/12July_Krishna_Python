items = []
print("WELCOME TO FRUIT MARKET".center(70))
empty_str = str()
print(empty_str)
print("1) Manager".center(55))
print("2) Customer".center(57))
print(empty_str)
display = input("Select Youe Role : ")
print(empty_str)
if display == '1':
    ch1='y'
    while(ch1=='y'):
        print("Fruit Market Manager".center(65))
        print(empty_str)
        print("1) Add Fruit Stock".center(63))
        print("2) View Fruit Stock".center(65))
        print("3) Update Fruit Stock".center(67))
        print("4) Exit".center(53))
        print(empty_str)
        choice = input("Enter your choice : ")
        if choice == '1':
            print("ADD FRUIT STOCK".center(60))
            item = {}
            item['name'] = input("Enter Fruit Name: ")
            item['quantity'] = int(input("Enter qty (in kg): "))
            item['price'] = int(input("Enter price (for kg): "))
            items.append(item)
            print(items)

        elif choice == '2':
            print("VIEW FRUIT STOCK".center(60))
            print('The number of fruits are: ',len(items))
            for item in items:
                for key, value in item.items():
                    print(key, ':', value)
                    
        elif choice == '3':
            print("UPDATE FRUIT STOCK".center(60))
            item_name = input('Enter the name of the fruit that you want to edit : ')
            for item in items:
                if item_name.lower() == item['name'].lower():
                    print('Here are the current details of ' + item_name)
                    print(item)
                    item['name'] = input('Fruit name : ')
                    item['quantity'] = int(input('Quantity : '))
                    item['price'] = int(input('Price $ : '))
                    print('Item has been successfully updated.')
                    print(item)
                else:
                    print('Item not found')
                
                        
        elif choice == '4':
            print("------------exited-----------")
            break
                
        else:
            print("please enter valid input...")
        select = input("Do you want to perform more operations : press y for yes and n for no : ")
        if select.lower() == 'y': 
            print(ch1)
        else:
            print("Thankyou!.....")
            break

        
        
