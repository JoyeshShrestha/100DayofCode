from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable
x = PrettyTable()
print("Hello! Welcome to Jo's CoffeeMachine.")
coffee_maker = CoffeeMaker()
menu = Menu()
def show_report():
    

    report = coffee_maker.report()

    print(report)
def receipt(coins,name,cost):
    change = coins - cost
    x.field_names = ["Order Name", "Total Cost"]
    x.add_row([name,str(cost)])
    x.add_row(["Tender: ",str(coins)])
    x.add_row(["Change: ", str(change)])
    print(x)



def recieve_coin(name,str_cost):
    proceed = True
    cost = float(str_cost)
    coins = 0
    while proceed:
        coins+=float(input("Please insert coins: "))
        
        if coins >= cost:
            receipt(coins,name,cost)
            print("Thank you for your patience")
            print("Your coffee is ready")
            break
            

        else:
            print("Insufficient Coins by",cost-coins)

def make_coffee():

    which_coffee = input("'l' for Latte, 'e' for espresso, 'c' for cappuccino: ").lower()
    if which_coffee == 'l':
        menu_items_name = "latte"
    elif which_coffee == 'e':
        menu_items_name = "espresso"
    elif which_coffee == 'c':
        menu_items_name = "cappuccino"        
    menu_item = menu.find_drink(menu_items_name)
    # print("++++++++++++",menu_item_obj)
    # menu_item = MenuItem(menu_item_obj) 

    if coffee_maker.is_resource_sufficient(menu_item):
        print(f"Total Cost for {menu_item.name}: {menu_item.cost}")
        recieve_coin(menu_item.name,menu_item.cost)
    else:
        print("Not Sufficent Ingredients")
        print(f"Required Ingredients: {menu_item.ingredients}")
        show_report()  

print("Choose a button:")
button = input("R for Report or M to Make Coffee: ").lower()
if button == "r":
    show_report()
else:
    make_coffee()






