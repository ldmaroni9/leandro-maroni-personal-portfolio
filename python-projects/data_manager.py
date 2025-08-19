import os
import requests
from dotenv import load_dotenv
from flight_search import FlightSearch

load_dotenv()

SHEET_API = os.getenv('SHEET_API')
HEADERS = os.getenv('HEADERS')
flight_searcher = FlightSearch()


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=f"{SHEET_API}/")
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def modify_sheet(self):
        for row in self.destination_data:
            iterated_city = row["ciudad"]
            new_value = flight_searcher.get_destination_code(city=iterated_city)
            requests.put(url=f'{SHEET_API}/{row["id"]}', json=new_value)



