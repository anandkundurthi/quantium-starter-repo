import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load formatted data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data by date
df = df.sort_values("date")

# Create line chart
fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time")

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),

    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
