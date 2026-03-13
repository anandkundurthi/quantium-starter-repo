import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.H1("Soul Foods Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#2c3e50"}),

    html.Div([
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"}
            ],
            value="all",
            labelStyle={"display": "inline-block", "margin": "10px"}
        )
    ], style={"textAlign": "center"}),

    dcc.Graph(id="sales-chart")

], style={"fontFamily": "Arial", "padding": "30px"})


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    filtered_df = filtered_df.sort_values("date")

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={"date": "Date", "sales": "Sales"}
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
