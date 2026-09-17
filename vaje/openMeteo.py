import requests

def najhladnejsi_dan(lat,lon):
    base_url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":lat,
        "longitude":lon,
        "daily":"temperature_2m_min"
    }
    callJSON = requests.get(base_url,params).json()
    najhladnejsi = [-1,100]
    for day in range(len(callJSON["daily"]["time"])):
        min_temp = callJSON["daily"]["temperature_2m_min"][day]
        if min_temp<najhladnejsi[1]:
            najhladnejsi[0] = callJSON["daily"]["time"][day]
            najhladnejsi[1] = min_temp
    return najhladnejsi




def najtoplejsi_dan(lat,lon):
    base_url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":lat,
        "longitude":lon,
        "daily":"temperature_2m_max"
    }
    callJSON = requests.get(base_url,params).json()
    najtoplejsi = [-1,-100]
    for day in range(len(callJSON["daily"]["time"])):
        max_temp = callJSON["daily"]["temperature_2m_max"][day]
    if max_temp>najtoplejsi[1]:
        najtoplejsi[0] = callJSON["daily"]["time"][day]
        najtoplejsi[1] = max_temp
    return najtoplejsi



def trenutna_temperatura(lat,lon):
    base_url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":lat,
        "longitude":lon,
        "current":"temperature_2m",
    }
    callJSON = requests.get(base_url,params).json()
    
    return callJSON["current"]["temperature_2m"]

def cel_teden_temperatura(lat,lon):
    base_url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":lat,
        "longitude":lon,
        "daily":"weather_code,temperature_2m_max,temperature_2m_min"
    }
    callJSON = requests.get(base_url,params).json()
    for day in range(len(callJSON["daily"]["time"])):
        min_temp = callJSON["daily"]["temperature_2m_min"][day]
        max_temp = callJSON["daily"]["temperature_2m_max"][day]
        difference = max_temp - min_temp
        print(callJSON["daily"]["time"][day]," - weather code: ",callJSON["daily"]["weather_code"][day], " | Min temperature: ",min_temp, ", Max temperature: ",max_temp, " , Difference: ", round(difference,1))



def main():
    print(najtoplejsi_dan(46.0569,14.5058))
#     base_url = requests.get("https://api.open-meteo.com/v1/forecast")

#     slovenian_cities_coords = {
#         "Ljubljana": {"latitude": 46.0569, "longitude": 14.5058},
#         "Maribor": {"latitude": 46.5547, "longitude": 15.6467},
#         "Celje": {"latitude": 46.2358, "longitude": 15.2675},
#         "Kranj": {"latitude": 46.2389, "longitude": 14.3556},
#         "Koper": {"latitude": 45.5469, "longitude": 13.7294},
#         "Velenje": {"latitude": 46.3623, "longitude": 15.1107},
#         "Novo Mesto": {"latitude": 45.8011, "longitude": 15.1710},
#         "Ptuj": {"latitude": 46.4200, "longitude": 15.8697},
#         "Kamnik": {"latitude": 46.2258, "longitude": 14.6121},
#         "Jesenice": {"latitude": 46.4355, "longitude": 14.0569}
#     }
#     print("Slovenian cityes:")
#     for city in slovenian_cities_coords:
#         print("- ",city)

#     mesto = input("Mesto: ")
#     if mesto in slovenian_cities_coords:

# ?latitude={slovenian_cities_coords[mesto]["latitude"]}&longitude={slovenian_cities_coords[mesto]["longitude"]}&daily=weather_code,temperature_2m_max,temperature_2m_min").json()

if __name__=="__main__":
    main()