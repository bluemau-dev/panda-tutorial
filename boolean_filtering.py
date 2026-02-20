import pandas as pd
import numpy as np

money = [20.11, 56.12, 70.25]
myvar = pd.Series(money)

data = {
    "My Money": myvar,
    "Cost of Goods": [5.99, 6.25, 1.99],
}

df = pd.DataFrame(data)
mask = df["My Money"] > 25.00
df[mask]
print(df[mask    ])
