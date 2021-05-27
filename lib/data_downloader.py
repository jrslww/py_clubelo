import requests
from io import StringIO
import pandas as pd
import numpy as np
from datetime import datetime

URL = 'http://api.clubelo.com/'

def getRanking():
    day = datetime.date(datetime.now())
    return showRanking(day)


def showRanking(day):
    url = requests.get(URL + str(day))
    data = StringIO(url.text)
    df = pd.read_csv(data, sep=",")
    return df


def plotCountry(tag):
    df = getRanking()
    lst = df.loc[df['Country'] == str(tag)]
    k = []
    for i in lst['Club']:
        j = i.replace(' ', '')
        k.append(j)

    return k


def getCountryElo(tag):
    fc_list = []
    for element in tag:
        fc_list.append(plotCountry(tag))
        print(fc_list)
    # return df["Elo"].mean()
    return fc_list


def plotClub(teamlist):
    fc_list = []
    data = StringIO()
    for element in teamlist:
        r = requests.get(URL + str(element))
        data = StringIO(r.text)
        df = pd.read_csv(data, sep=",")
        fc_list.append(df)
    return pd.concat(fc_list)