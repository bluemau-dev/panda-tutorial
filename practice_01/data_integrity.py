import pandas as pd
import numpy as np

#Practice with CSV Files
df = pd.read_csv('pandas_practice_dataset.csv')

# Verify if Customer Paid Entirely
verify_price = df["total_price"] != (df['quantity'] * df['unit_price']).round(2)
price_validation = df[verify_price]

#print(len(price_validation))

# Creates a Series from a Data Frame
trasnactions_per_customer = df.groupby("customer_id")["order_id"].count()
print(trasnactions_per_customer)

my_val = df.groupby("customer_id").size()
print(my_val)

# Creating a Data Frame from a Data Frame
t = (
    df.groupby("customer_id")
    .size()
    .reset_index(name="transaction_count")
    .sort_values("transaction_count", ascending=False)
)
