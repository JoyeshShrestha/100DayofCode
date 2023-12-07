# with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day025_CSV\\weather_data.csv") as csv_file:
#     file = csv_file.readlines()
#     print_file = []
#     for f in file:
#         print_file.append(f.strip())
#     print(print_file)


# import csv

# with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day025_CSV\\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             pass
#     print(temperatures)   

import pandas

data = pandas.read_csv("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day025_CSV\\weather_data.csv")

# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list)/len(temp_list)

#get data in Row
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print((monday["temp"][0] * 9/5)+32)



#Create a dataframe from scratch




