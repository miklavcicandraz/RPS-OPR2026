import requests

def trenutna_temperatura(lat,lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=auto&forecast_days=1"
    callJSON = requests.get(base_url).json()
    print(callJSON["current"]["temperature_2m"])



trenutna_temperatura(46.12,14.5)

