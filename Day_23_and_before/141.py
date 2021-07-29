# from turtle import Turtle, Screen
#
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("chartreuse")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()
from prettytable import PrettyTable


# table = PrettyTable()
# table.add_column("Pokemon name",
#                  ["Picachu", "Squirtle", "Charmander"])
# table.add_column("Type",
#                  ["Electric", "Water", "Fire"])
# print(table)

table2 = PrettyTable()
table2.field_names = ["Pokemon name", "Type"]
table2.add_row(["Picachu", "Electric"])
table2.add_row(["Squirtle", "Water"])
table2.add_row(["Charmander", "Fire"])
print(table2)
table2.sortby = "Pokemon name"
print(table2)
table2.align = "r"
print(table2)
