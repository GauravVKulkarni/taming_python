import requests
from dotenv import load_dotenv
from os import getenv
import json

load_dotenv()
BASE_URL = getenv("BASE_URL")
API_KEY = getenv("API_KEY")
CITY = getenv("CITY")


url = BASE_URL+"/current.json"


params = {
    "key": API_KEY,
    "q": CITY
}

res = requests.get(url, params=params)
data = res.json()

data_file = "./data.json"
with open (data_file, 'w') as f:
    json.dump(data, f, indent=4)