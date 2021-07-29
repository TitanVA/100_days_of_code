# data = []
#
# with open("212 weather-data.csv") as f:
#     file = f.readlines()
#     for line in file:
#         strip_line = line.strip("\n")
#         data.append(strip_line)
#
# print(data)
# import csv
#
#
# with open("212 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
import pandas
from statistics import mean


# data = pandas.read_csv("212 weather-data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# mean_list = mean(temp_list)
# print(round(mean_list, 2))
#
# temp_list2 = data["temp"].to_list()
# average_num = sum(temp_list2) / len(temp_list2)
# print(round(average_num, 2))
#
# average = data["temp"].mean()
# print(round(average, 2))
#
# max_num = data["temp"].max()
# print(max_num)

# max_temp = data["temp"].max()
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# f_temp = (int(monday.temp) * 9 / 5) + 32
# print(round(f_temp, 2))

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

"""My solving"""
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
# cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
# black_squirrel = data[data["Primary Fur Color"] == "Black"]
# number_of_gray = len(gray_squirrel)
# number_of_cinnamon = len(cinnamon_squirrel)
# number_of_black = len(black_squirrel)
# numbers_of_squirrel = [number_of_gray, number_of_cinnamon, number_of_black]
# colors_list = data['Primary Fur Color'].unique()[1:]
# exit_data = pandas.DataFrame({
#     "Color": colors_list,
#     "Num": numbers_of_squirrel,
# })
#
# exit_data.to_csv("exit_data.csv")


"""Lesson solution"""
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur_color = data["Primary Fur Color"]
gray_squirrel_count = len(data[primary_fur_color == "Gray"])
red_squirrel_count = len(data[primary_fur_color == "Cinnamon"])
black_squirrel_count = len(data[primary_fur_color == "Black"])
data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
