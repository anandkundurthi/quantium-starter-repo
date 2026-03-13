import pandas as pd

# Load all CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine datasets
df = pd.concat([df1, df2, df3])

# Filter Pink Morsel
df = df[df["product"] == "pink morsel"]

# Clean price column
df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)

# Calculate sales
df["sales"] = df["price"] * df["quantity"]

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Split before and after 15 Jan 2021
before = df[df["date"] < "2021-01-15"]["sales"].sum()
after = df[df["date"] >= "2021-01-15"]["sales"].sum()

print("Sales before 15 Jan 2021:", before)
print("Sales after 15 Jan 2021:", after)
