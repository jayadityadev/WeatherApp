def request_handler(city):
    import requests
    import json
    url = f"https://api.weatherapi.com/v1/current.json?key=4e980aa1fa2447b782b153807230409&q={city}&aqi=no"
    response = requests.get(url)
    response_dictionary = json.loads(response.text)
    return response_dictionary


def weather(city):
    place = request_handler(city)["location"]["name"]
    condition = request_handler(city)["current"]["condition"]["text"]
    temp_c = request_handler(city)["current"]["temp_c"]
    temp_f = request_handler(city)["current"]["temp_f"]
    local_time = request_handler(city)["location"]["localtime"]
    if request_handler(city)["current"]["is_day"] == 1:
        day_night = "Day"
    else:
        day_night = "Night"
    return {"place": place, "weather": condition, "temp_c": temp_c, "temp_f": temp_f,
            "local_time": local_time, "day_night": day_night}
