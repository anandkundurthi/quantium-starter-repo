import pandas as pd

# Load CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine datasets
df = pd.concat([df1, df2, df3])

# Keep only Pink Morsel
df = df[df["product"] == "pink morsel"]

# Clean price column
df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)

# Create sales column
df["sales"] = df["price"] * df["quantity"]

# Keep required columns
df = df[["sales", "date", "region"]]

# Save output file
df.to_csv("formatted_sales_data.csv", index=False)
