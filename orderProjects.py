#For showing menu in which dish name and the price of that dish will be mentioned so for that we can use the dictionary thing
menu ={
     'Pizza': 50,
     'Burger': 40,
     'Cold Drink': 30,
     'Ice-Cream': 100,
     'Coffee laaateeee': 1000
     
     
     
 }


print("Welcome to the PYTHON Restaurant")
print(" Pizza:50\n Burger:40\n Cold Drink:30\n Ice-Cream:100\n Coffee laaaate:1000")
orderTotal=0
item1 = input("Enter the name of the dish you want to order:")
if item1 in menu:
    orderTotal+= menu[item1]
    print(f"Your item {item1} has been added to your order")
else:
    print(f"Ordered item {item1} is not avaiable yet")


anotherOrder = input("Do you want to order anything else:")
if anotherOrder=="Yes":
    item2 = input("Enter the name of the dish you want to order:")
if item2 in menu:
    orderTotal+= menu[item2]
    print(f"Your item {item2} has been added to your order")
else:
    print(f"Ordered item {item2} is not avaiable yet")

    
