country = input("Enter which country have you been to. ")
visits= int(input("How many times have you visited that country?  "))
list_of_cities = []
n=0
while n ==0:
    city = input("Enter the list of cities. ")
    list_of_cities.append(city)
    proceed = input("Do you want to continue? Y/N  ").lower()
    if proceed == "n":
        break

travel_log = [
    {
        "country":"France",
        "visits" : 12,
        "cities" : ["Paris","Lille","Dijon"]
    },
    {
       "country":"Germany",
        "visits" : 5,
        "cities" : ["Berlin","Hamburg"]
    },
]

print(travel_log[1]["visits"])

travel_diction = {}
def add_new_country(country, visits, list_of_cities):
    travel_diction["country"]=country
    travel_diction["visits"]=visits
    travel_diction["list_of_cities"]=list_of_cities

    travel_log.append(travel_diction)
    print (f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times")
    print(f"My favourite city was {travel_log[2]['list_of_cities'][0]}")

add_new_country(country, visits, list_of_cities)

