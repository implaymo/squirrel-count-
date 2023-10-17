import csv

import pandas
import pandas as pd
from pandas import DataFrame
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     temperatures.pop(0)
#     temperatures = list(map(int, temperatures))
#
# data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"].to_list()
# data_dict = data.to_dict()
# print(data_dict)

# total_temp = 0
# for data in data_list:
#     total_temp += data
#     average = total_temp / len(data_list)
# print(average)


# print(data_list.to_list())
#
# average = data_list.mean()
#
# print(data[data.day == "Monday"])
# max_value = data.temp.max()
# row_max_value = data[data.temp == max_value]
# print(row_max_value)
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = data[data.day == "Monday"]
# monday_temp_f = monday_temp.temp * 1.8 + 32
# print(monday_temp_f)

import pandas

# Main file data frame
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231014.csv")

# Gets the amount of every color
fur_colors = data["Primary Fur Color"]
fur_colors_counts = fur_colors.value_counts()

# Creates a new data frame to hold color values and amounts
new_data_frame = pandas.DataFrame({'fur color': fur_colors_counts.index, 'count': fur_colors_counts.values})

# Creates new data frame as a CSV file
new_data_frame.to_csv("squirrel_count.csv")



