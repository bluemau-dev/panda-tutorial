import numpy as np
import pandas as pd

mango = [5,3,2,4]
apple = [4,3,7,2]
banana = [8,10,11,2]

myvar = pd.Series(mango)
myvar2 = pd.Series(apple)
myvar3 = pd.Series(banana)

data = {
    "Mango": myvar,
    "Apple": myvar2,
    "Banana": myvar3,
}

df = pd.DataFrame(data)
print(df.loc[[0,1,2]])