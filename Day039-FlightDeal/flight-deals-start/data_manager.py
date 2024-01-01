import requests
SHEETY_API = "https://api.sheety.co/c3d7f3385565659f15f302b3f8c6e736/flightDeals/prices"

# test = {'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        pass


    def get_data(self):
        # self.response = requests.get(url=SHEETY_API)
        # self.present_data = self.response.json()
        # print(self.present_data)
        # data_lists = self.present_data['prices']

        # ok = test['prices']

        # IATA_code = {yo['iataCode']:yo['lowestPrice'] for yo in data_lists}
        IATA_code = {'PAR': 60000, 'BER': 30000, 'TYO': 25000, 'SYD': 49386, 'IST': 43567, 'KUL': 28754, 'NYC': 87307, 'SFO': 90195, 'CPT': 63343}
        self.code_dict = {}
        
        
        return IATA_code
        
        # self.id = [id for id in self.present_data["prices"]] 
    def update_data(self,id):
        body = {
            "price":{

            }
        }
        self.response= requests.put(url=f"https://api.sheety.co/c3d7f3385565659f15f302b3f8c6e736/flightDeals/prices/{id}",data=body)   

    
        