
import requests


def get_weather_data(city_name, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        print("Weather Data for", city_name)
        print("Tmperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
        print("Humidty:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


def main():
    print('WELCOME TO WEATHER KNOW CODE'.center(50))
    name = input('Enter your name: ')
    name_city = input('If you want to see the available city names for help, enter "yes": ')

    city_list = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
                 "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
                 "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
                 "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
                 "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
                 "National Capital Territory of Delhi", "Puducherry"]

    if name_city.lower() == 'yes':
        print('there  are the names of the cities whose weather you can find:\n', city_list)

    while True:
        city = input('Enter the city name to find weather:').strip().title()
        if city in city_list:
            API_key = 'c2be590077f37537201ffb60e6e6a1f6'
            get_weather_data(city, API_key)
        else:
            print('Wrong city name entered, please try again.')

        retry = input('Do you want to check another city? (yes/no): ').strip().lower()
        if retry != 'yes':
            break

    print(f'Thank you {name} for visiting my code home'.center(40))


if __name__ == '__main__':
    main()
