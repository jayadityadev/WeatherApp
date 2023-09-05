from functions import weather


if __name__ == '__main__':

    print("\nWelcome to Weather App. Created by Jayaditya Dev in Python.")
    city = input("Enter the name of the City: ")

    print(f"\nPlace: {weather(city)['place']}")
    print(f"Weather: {weather(city)['weather']}")
    print(f"Temperature: {weather(city)['temp_c']}°C / {weather(city)['temp_f']}°F")
    print(f"Local Time: {weather(city)['local_time']}")
    print(f"Day/Night: {weather(city)['day_night']}")

    print("\nThank You!")
