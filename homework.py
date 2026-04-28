import pandas as pd

data = pd.read_csv("airbnb.csv")

data['price'] = data['price'].str.replace('$', '', regex=False)
# alternatively str.strip('$')

data["price"] = pd.to_numeric(data["price"])
# convert to numeric = float/int
data['price'] = pd.cut(data['price'], bins=5) # <----------------- pd.cut

frequency_table = data["price"].value_counts().sort_index()

print(frequency_table)
