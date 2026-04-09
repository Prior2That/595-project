import plotly.graph_objects as go

categories = [] #Names of each category
n = 5 #Highest Value

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[], # values for each category (number 0-n)
    theta=categories,
    fill='toself',
    name='' #name of object A
))

# For second Plot
fig.add_trace(go.Scatterpolar(
    r=[], # values for each category (number 0-n)
    theta=categories,
    fill='toself',
    name='' # name of object B
))

fig.update_layout(polar=dict(
    radialaxis=dict(visible=True,
                    range=[0,n])),
                    showlegend=False)

fig.show()