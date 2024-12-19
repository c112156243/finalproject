import os
import requests
from dotenv import load_dotenv
import pandas as pd
def get_weather_data_ChanghuaCounty():
    url=os.getenv('ChanghuaCounty')
    response = requests.get(url)
    data=response.json()
    df=pd.DataFrame(data)
    return df
