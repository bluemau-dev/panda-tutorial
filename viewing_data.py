import numpy as np
import pandas as pd

dates = pd.date_range("20260219", periods=4)
df = pd.DataFrame(np.random.randn(4,4), index=dates, columns=list("ABCD"))

print(df)
#print(df.head)
#print(df.tail)
#print(df.index)
#print(df.columns)