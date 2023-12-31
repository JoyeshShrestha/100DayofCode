from flight_search import FlightSearch
class FlightData(FlightSearch):
    #This class is responsible for structuring the flight data.
    def __init__(self,l):
        self.l = l
        
        super().__init__()

    def improve_data(self,lower_prices):
        cleaned_data = []
        
        for info in lower_prices:
            cleaned_data_dict={}

            cleaned_data_dict["countryTo"] = info["cityTo"]
            cleaned_data_dict["price"] = info["price"]
            cleaned_data_dict["availability"]=info["availability"]
            cleaned_data.append(cleaned_data_dict)
        print("=======",cleaned_data)
        return cleaned_data

