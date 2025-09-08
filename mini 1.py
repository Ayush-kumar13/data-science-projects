import requests

api_key = "5b612ee8644754aef5526fd2136ca1a5"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("CITY NOT FOUND, PLEASE TRY AGAIN")
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        print(f"\nWeather in {city_name}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {description.capitalize()}\n")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    city = input("ENTER THE CITY NAME: ")
    get_weather(city)
