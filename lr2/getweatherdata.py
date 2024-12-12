import requests 
class QueryError(Exception):
    pass

from owm_key import owm_api_key

def get_weather_data(place, api_key=None):
    # напишите здесь ваш код
    if place == '' or api_key is None:
        return

    try:
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}')

        res_data = res.json()

        if res_data['cod'] != 200:
            raise QueryError(res_data['message'])


        data = dict()
        data['name'] = res_data['name']
        data['country'] = res_data['sys']['country']
        data['coord'] = res_data['coord']

        ts = res_data['timezone'] // 3600
        if ts > 0:
            timezone_str = f'UTC+{ts}'
        else:
            timezone_str = f'UTC{ts}'
        data['timezone'] = timezone_str
        temp = res_data['main']['feels_like']
        temp_c = round(temp - 273.15, 2)
        data['feels_like'] = temp_c

        json_data = json.dumps(data)
        return json_data

    except QueryError as e:
        print('request failed:', e)

    except requests.exceptions.RequestException as e:
        print('request failed:', e)

    
if name == "__main__":
    print(get_weather_data("Chicago", owm_api_key))
    print(get_weather_data("Saint Petersburg", owm_api_key))
    print(get_weather_data("Dhaka", owm_api_key))   

from owm_key import owm_api_key
import json