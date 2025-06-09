import os
import pandas as pd
import matplotlib.pyplot as plt

# I can't properly write and debug this without your data.

# Do you really need hourly data from 1995 to 2024? Could you do the same with daily data?
# If so, do a little pre-processing to get the data into a more manageable format.


def get_cleaned_yearly_avg(file_path, location):
    df = pd.read_csv(file_path, parse_dates = ["DATE"], low_memory=False)
    
    df = df.dropna(subset=['DailyMaximumDryBulbTemperature', 'DailyMinimumDryBulbTemperature'])
    df['TAVG'] = (df['DailyMaximumDryBulbTemperature'] + df['DailyMinimumDryBulbTemperature']) / 2
    df['YEAR'] = df['DATE'].dt.year

    df["location"] = location

    yearly_avg = df.groupby('YEAR')['TAVG'].mean().reset_index()
    return yearly_avg[(yearly_avg['YEAR'] >= 1997) & (yearly_avg['YEAR'] <= 2024)]


def load_data(city_files):
    return pd.concat(
        [get_cleaned_yearly_avg(file_path, city) for city, file_path in city_files.items()],
        ignore_index=True
    )


