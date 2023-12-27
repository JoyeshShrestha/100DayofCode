# from turtle import Turtle , Screen


# johnny =Turtle()
# print(johnny)
# johnny.shape("turtle")
# johnny.color("purple")
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
x = PrettyTable()

x.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander","Bulbasaur"])
x.add_column("Type",["Electric","Water","Fire","Grass"])
x.align = "l"
print(x)