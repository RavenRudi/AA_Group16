import pandas as pd
import numpy as np
import math

# Global constants that are used in multiple notebooks
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

point_of_day = ["morning", "afternoon", "evening", "night"]

morning_hours = [*range(6, 12)]
afternoon_hours = [*range(12, 18)]
evening = [*range(18, 23)]
night = [23] + [*range(0, 6)]

temperature_points = ["very hot (29+)", "hot (24-28)", "good (16-23)", "cold (8-15)", "very cold(7-)"]

very_hot = [*range(29, 45)]
hot = [*range(24, 29)]
good = [*range(16, 24)]
cold = [*range(8, 16)]
very_cold = [*range(-30, 8)]


# Functions

# This functions loads the prepared weather data and determines the correct datatypes for each columns
def load_prepared_data():
    df_boston = pd.read_csv('./data/prepared/rides_data_prepared_weather.csv',
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


# This function divides the temperatures into 5 parts and returns level of temperature
def get_level_of_temperature(temperature):
    if type(temperature) == float and not math.isnan(temperature):
        temperature = round(temperature)
        if temperature in very_hot:
            return "1_very_hot"
        elif temperature in hot:
            return "2_hot"
        elif temperature in good:
            return "3_good"
        elif temperature in cold:
            return "4_cold"
        elif temperature in very_cold:
            return "5_very_cold"


def get_middle_of_two_numbers(number_a, number_b):
    return (number_a + number_b) / 2
