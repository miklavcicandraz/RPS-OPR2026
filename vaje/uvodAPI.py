import requests


base_url = "https://api.chucknorris.io/jokes/random"

call = requests.get(base_url)
#print(call.text)

callJSON = call.json()

print(callJSON["value"])
