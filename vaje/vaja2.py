import requests


slovenian_cities_coords = {
    "Ljubljana": {"latitude": 46.0569, "longitude": 14.5058},
    "Maribor": {"latitude": 46.5547, "longitude": 15.6467},
    "Celje": {"latitude": 46.2358, "longitude": 15.2675},
    "Kranj": {"latitude": 46.2389, "longitude": 14.3556},
    "Koper": {"latitude": 45.5469, "longitude": 13.7294},
    "Velenje": {"latitude": 46.3623, "longitude": 15.1107},
    "Novo Mesto": {"latitude": 45.8011, "longitude": 15.1710},
    "Ptuj": {"latitude": 46.4200, "longitude": 15.8697},
    "Kamnik": {"latitude": 46.2258, "longitude": 14.6121},
    "Jesenice": {"latitude": 46.4355, "longitude": 14.0569}
}
print("Slovenian cityes:")
for city in slovenian_cities_coords:
    print("- ",city)

mesto = input("Mesto: ")
if mesto in city:
    result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={slovenian_cities_coords[mesto]["latitude"]}&longitude={slovenian_cities_coords[mesto]["longitude"]}&daily=weather_code").json()

for i in range(len(result["daily"]["time"])):
    print(result["daily"]["time"][i]," - ",result["daily"]["weather_code"][i])