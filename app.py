# Plotly Dash dashboard for SpaceX launch records
# Run:  python app.py   (needs spacex_launch_dash.csv in the same folder)
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv("spacex_launch_dash.csv")
min_p, max_p = df["Payload Mass (kg)"].min(), df["Payload Mass (kg)"].max()

app = dash.Dash(__name__)
sites = [{"label": "All Sites", "value": "ALL"}] + [
    {"label": s, "value": s} for s in sorted(df["Launch Site"].unique())]

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", style={"textAlign": "center"}),
    dcc.Dropdown(id="site-dropdown", options=sites, value="ALL",
                 placeholder="Select a Launch Site", searchable=True),
    html.Br(),
    dcc.Graph(id="success-pie-chart"),
    html.P("Payload range (kg):"),
    dcc.RangeSlider(id="payload-slider", min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)},
                    value=[min_p, max_p]),
    dcc.Graph(id="success-payload-scatter-chart"),
])

@app.callback(Output("success-pie-chart", "figure"),
              Input("site-dropdown", "value"))
def pie(site):
    if site == "ALL":
        return px.pie(df[df["class"] == 1], names="Launch Site",
                      title="Total successful launches by site")
    d = df[df["Launch Site"] == site]["class"].value_counts().reset_index()
    d.columns = ["class", "count"]
    return px.pie(d, names="class", values="count",
                  title=f"Success (1) vs failure (0) for {site}")

@app.callback(Output("success-payload-scatter-chart", "figure"),
              [Input("site-dropdown", "value"), Input("payload-slider", "value")])
def scatter(site, rng):
    d = df[df["Payload Mass (kg)"].between(rng[0], rng[1])]
    if site != "ALL":
        d = d[d["Launch Site"] == site]
    return px.scatter(d, x="Payload Mass (kg)", y="class",
                      color="Booster Version Category",
                      title="Payload vs outcome")

if __name__ == "__main__":
    app.run(debug=True)
