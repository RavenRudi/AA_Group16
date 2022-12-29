import pandas as pd
import numpy as np

# Global constants that are used in multiple notebooks
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

point_of_day = ["morning", "afternoon", "evening", "night"]

morning_hours = [*range(6, 12)]
afternoon_hours = [*range(12, 18)]
evening = [*range(18, 23)]
night = [23] + [*range(0, 6)]


# Functions

# This functions loads the prepared weather data and determines the correct datatypes for each columns
def load_prepared_data():
    df_boston = pd.read_csv('./data/prepared/rides_data_prepared_waether.csv',
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
    return df_boston


# This function divides the day into four parts and returns the point of day from the given hour of day
def get_point_of_day(hour):
    if hour in morning_hours:
        return "1_morning"
    elif hour in afternoon_hours:
        return "2_afternoon"
    elif hour in evening:
        return "3_evening"
    elif hour in night:
        return "4_night"
