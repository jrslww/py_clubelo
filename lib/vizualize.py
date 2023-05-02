import pandas as pd
import plotly.express as px

def plot_club_elo(club_list, df):
    fig = px.line(df, x='From', y='Elo', color='Club', title='Club ELO Ratings Over Time')
    fig.show()
