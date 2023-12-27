import pandas

data = pandas.read_csv("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day025_CSV\\thegreatsquirrel\\squirrel_data.csv")


fur = data["Primary Fur Color"]
# print(fur)
gray = fur[fur == "Gray"].to_list()
cinnamon = fur[fur == "Cinnamon"].to_list()

# print(gray)
data_dict = {
    "Fur Color": ["Gray","Cinnamon"],
    "Count":[len(gray),len(cinnamon)]


}

final_data = pandas.DataFrame(data_dict)

print(final_data)
