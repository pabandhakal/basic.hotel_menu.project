# Define the menu of restaurent

menu={
    "Rice": 50,
    "Tea":  10,
    "Pasta":60,
    "Role": 40,
    "coffe":30,
    "Pizza":100
}
print(menu)

#great

print("Wellcome to M.K Restaurent")
print(" Rice: Rs 50\n Tea: Rs 10\n Pasta: Rs 60\n Role: Rs 40\n Coffe: Rs 30\n Pizza: Rs 100")

order_total=0


item_1 =input("Enter the name of item you want to order =")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f" Ordered item {item_1} is not available yet !")

another_order = input("Do you want to another item ? (Yes/No)")
if another_order =="Yes":
    item_2= input("Enter the name of second item =")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item (item_2) is not available!")

print(f"The total amount of items to pay is {order_total}")