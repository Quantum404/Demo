import numpy as np
import pandas as pd
weather_data = pd.read_csv("testset.csv")
weather_data.rename(columns={'_conds': 'conditions'}, inplace=True,axis='columns')