import numpy as np
import pandas as pd
weather_data = pd.read_csv("testset.csv")
# Delete a single column from the DataFrame
weather_data = weather_data.drop(labels=[" _windchillm", " _wspdm"], axis=1)

#Convert from object datatype to datetime format
weather_data['datetime_utc'] = pd.to_datetime(weather_data['datetime_utc'])
#Filtering data from date:1999-12-15
weather_filtered = weather_data.loc[weather_data['datetime_utc'] > '1999-12-15']

