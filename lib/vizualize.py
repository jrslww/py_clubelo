import plotly.express as px

fig1 = px.line(plotClub(['Villarreal', 'Shakhtar']), x = 'From', y = 'Elo', title= 'Clubelo Ranking', color = 'Club')
fig1.show()