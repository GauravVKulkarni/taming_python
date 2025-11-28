# trial and testing ground

import requests

url = "https://api.toys/api/coin_flip"
res = requests.get(url)

print(res)
res_data = res.json()
print(res_data)