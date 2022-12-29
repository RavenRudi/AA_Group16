import pandas as pd
import numpy as np




# Functions

def foo():
    return "foo"


def load_prepared_data():
    print("called")
    df_boston = pd.read_csv('../data/prepared/rides_data_prepared_waether.csv',
                            dtype={
                                'start_station_id': np.int64,
                                'end_station_id': 'string',
                                'end_station_name': 'string',
                                'start_station_name': 'string',
                                'bike_id': np.int64,
                                'user_type': 'string',
                                'max_temp': np.float64,
                                'min_temp': np.float64,
                                'precip': np.float64
                            })
    df_boston['start_time'] = pd.to_datetime(df_boston['start_time'], format='%Y-%m-%d %X')
    df_boston['end_time'] = pd.to_datetime(df_boston['end_time'], format='%Y-%m-%d %X')
    df_boston.drop(index=df_boston.loc[df_boston["end_station_id"] == "\\N"].index, inplace=True, axis=1)
    print(df_boston.head())
    return df_boston



