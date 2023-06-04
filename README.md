# WeaterForecastor

This code is able to generate an API in localhost for users to forecast the temperature of Dhaka 24 hours ahead starting from the present time using a ARMA model

<br>

The development of this code was in Linux environment. It is unclear for other environments as it has not been tested for those.

<br>

To use this, you need to create a virtual environment using the following command. Also, you need to have Python 3.10. 

<br>

First clone the repository. Then, open up a terminal, and go to the directory where you saved it. Run the following command:


```

python3 -m venv /home/test/weather

```

<br>

Afterwards, you run the following command to install the requirements

<br>

```

pip install -r requirements.txt

```


This will install all the requirements to the environment to run the file. 


<br> 

And then, you just run the DhakaTemperatureForecast.py.


<br>


```

python DhakaTemperatureForecast.py

```


You fire up a browswer tab and enter this URL:  http://127.0.0.1:5000/api/dhakaWeather

And you have your API to know the temperature




If you want to know about how the model is run, you can view the WeatherForecast.ipynb file. This will show the details of how the model was created.
