import urllib.request
import os
import pandas as pd
from sqlalchemy import create_engine, types
import sqlite3
from zipfile import ZipFile

def download_data():
    url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
    file = "stops.txt"
    temp_file = "exercise5.zip"
    temp_dir = "exercise5"

    urllib.request.urlretrieve(url, temp_file)
    with ZipFile(temp_file, 'r') as zip:
        zip.extractall(temp_dir)

    return os.path.join(temp_dir, file)


def load_data(path):
    cols = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]
    df = pd.read_csv(path, sep=",", encoding="utf-8", usecols=cols)
    return df


def transform_data(df):
    return df.query("(zone_id == 2001) and (-90 <= stop_lat <= 90) and (-90 <= stop_lon <= 90)")


def store_data(df):
    sql_dtype = {
        'stop_id': types.INT,
        'stop_name': types.TEXT,
        'stop_lat': types.FLOAT,
        'stop_long': types.FLOAT,
        'zone_id': types.INT,
    }

    engine = create_engine('sqlite:///gtfs.sqlite', echo=False) 
    df.to_sql(name='stops', con=engine, index=False, if_exists='replace', dtype=sql_dtype)
    engine.dispose()


def main():
    data_path = download_data()
    data = load_data(data_path)
    df = transform_data(data)
    store_data(df)


if __name__ == "__main__":
    main()