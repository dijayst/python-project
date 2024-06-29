
import requests
import json

# country_name = input("enter a the name of a country")

def get_data(url):
    response = requests.get(url, 
                            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    # A conditional statement to check if it connected to the api or not
    # if its connected we only get some of the data which was printed in main_weather
    if response.status_code == 200:
        data = response.json()
        print(data)
        #print(response.text)
       
        main_weather = {
            "location_name": data.get('name'),
            "coordinates": data.get('coord'),
            "temperature": data.get('main').get('temp'),
            "pressure": data.get('main').get('pressure'),
            "humidity": data.get('main').get('humidity'),
            "wind_speed": data.get('wind').get('speed')
        }
        #print(json.dumps(main_weather, indent=4))
      
    else:
        print(f"Failed to get data from {url}")
      
    
get_data("https://api.openweathermap.org/data/2.5/weather?lat=6.60&lon=3.34&appid=b17f7e1fa988f93d725139581b2d034a")
