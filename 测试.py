# -*- coding : utf-8 -*-
from random import *
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['Beijing', 'Shanghai', 'Guangzhou']}
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
print(df)


