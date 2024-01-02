#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_data import FlightData

google_sheet = DataManager()
list_IATA=google_sheet.get_data()
print("SAUUUUUUU",list_IATA)

kiwiflight = FlightSearch()
# list_IATA=[{'Berlin': 48512}, {'Paris': 51563}, {'New York': 86901}, {'Kuala Lumpur': 28200}, {'Sydney': 49380}, {'Istanbul': 43339}, {'San Francisco': 89684}, {'Cape Town': 63122}, {'Tokyo': 42523}]
new_prices,is_lower,l_price = kiwiflight.get_flight_info(list_IATA)
print("NEW PRICES",new_prices)
print(f"YOOOOOOOOOOO{kiwiflight.is_lower}")
print(f"YOOOOOOOOOOO{l_price}")

if is_lower:
    notification = NotificationManager(l_price)
