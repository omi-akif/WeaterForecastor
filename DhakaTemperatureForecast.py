import pytz
import pickle
import requests
import pandas as pd
from flask import Flask
from datetime import datetime, timedelta




#Creating a app object with the Flask class and __name__ argument used for constructor

app = Flask(__name__)


# Make a request to the Open-Metro API

response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=23.71&longitude=90.41&hourly=temperature_2m&past_days=7&forecast_days=0&timezone=Asia%2FSingapore')

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    temp = data['hourly']['temperature_2m']

    date = data['hourly']['time']
    
    # Convert the data into a DataFrame
    
else:

    print('Error:', response.status_code)


# Input datetime string
datetime_string = date[-1]

# Convert datetime string to datetime object
datetime_obj = datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M")

# Set the timezone to "Asia/Singapore"
singapore_timezone = pytz.timezone("Asia/Singapore")
datetime_obj = singapore_timezone.localize(datetime_obj)

# Convert the timezone to "Asia/Dhaka"
dhaka_timezone = pytz.timezone("Asia/Dhaka")
datetime_obj_dhaka = datetime_obj.astimezone(dhaka_timezone)

# Generate hourly date and time strings for the next 24 hours in "Asia/Dhaka" timezone
hourly_date_times = []
for i in range(24):
    hourly_date_times.append(datetime_obj_dhaka.strftime("%Y-%m-%dT%H:%M"))
    datetime_obj_dhaka += timedelta(hours=1)




filename = 'TemperatureForecast.pkl'

with open(filename, 'rb') as f:
    weatherForecaster = pickle.load(f)

temp = weatherForecaster.forecast(steps = 24)

predTempDataFrame = pd.DataFrame({'Hourly': hourly_date_times, 'Temp' : temp})

# print(predTempDataFrame)



@app.route('/api/dhakaWeather', methods=['GET'])

def hello():
    return predTempDataFrame.to_json()


if __name__ == '__main__':
    app.run()