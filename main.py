from turtle import Turtle, Screen
#from prettytable import PrettyTable

import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == '__main__':
    # timmy = Turtle()
    # timmy.shape("turtle")
    # timmy.color("red")
    # timmy.forward(100)
    # timmy.left(120)
    # timmy.forward(100)
    # timmy.left(120)
    # timmy.forward(100)
    #
    # my_screen = Screen()
    # my_screen.canvheight = 10
    # my_screen.canvwidth = 10
    # my_screen.exitonclick()

    #
    # table = PrettyTable()
    #
    # table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    # table.add_column("Type", ["Electric", "Water", "Fire"])
    # table.align ="l"
    # print(table)


# Doing coffee machine project with OOP
    my_coffee_maker = CoffeeMaker()
    mu_money_machine = MoneyMachine()
    my_menu = Menu()


    while (True):
        avilable_drinks = my_menu.get_items()
        choice = input(f"What would you like? ({avilable_drinks}): ").lower()
        match choice:
            case "report":
                my_coffee_maker.report()
                mu_money_machine.report()
            case "off":
                break
            case "espresso" |"latte" |"cappuccino": # multiple
                enough_resource = my_coffee_maker.is_resource_sufficient((my_menu.find_drink(choice)))
                if enough_resource:
                    enough_money = mu_money_machine.make_payment(float(my_menu.find_drink(choice).cost))
                    if enough_money:
                        my_coffee_maker.make_coffee((my_menu.find_drink(choice)))
            case _:
                print("Wrong choice. Try again !")
                pass



