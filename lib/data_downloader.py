import requests
import pandas as pd
from datetime import datetime
from io import StringIO

URL = 'http://api.clubelo.com/'

def get_ranking(date=None):
    if date is None:
        date = datetime.now().date()
    url = requests.get(URL + str(date))
    if url.status_code == 200:
        data = StringIO(url.text)
        df = pd.read_csv(data, sep=",")
        return df
    else:
        print(f"Error: {url.status_code}")
        return None

def filter_by_country(df, country_tag):
    return df.loc[df['Country'] == country_tag]

def get_club_data(club_list):
    dfs = []
    for club in club_list:
        r = requests.get(URL + club)
        if r.status_code == 200:
            data = StringIO(r.text)
            df = pd.read_csv(data, sep=",")
            dfs.append(df)
        else:
            print(f"Error fetching data for {club}: {r.status_code}")
    return pd.concat(dfs)