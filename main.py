from functions import weather

if __name__ == '__main__':
    try:
        print("\nWelcome to Weather App. Created by Jayaditya Dev in Python.")
        city = input("Enter the name of the City: ")
        weather_dic = weather(city)
        print(
                f"\nPlace: {weather_dic['place']}, {weather_dic['region']}, {weather_dic['country']}\n"
                f"Weather: {weather_dic['weather']}\n"
                f"Temperature: {weather_dic['temp_c']}°C / {weather_dic['temp_f']}°F\n"
                f"Local Time: {weather_dic['local_time']}\n"
                f"Day/Night: {weather_dic['day_night']}\n"
                f"\n[Last updated on {weather_dic['last_updated']}]"
              )
        print("\nThank You!")
    except KeyError:
        print("\nPlease enter a valid city name.")
