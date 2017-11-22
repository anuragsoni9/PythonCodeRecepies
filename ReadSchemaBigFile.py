import os
import pandas as pd
chunksize = 10
for chunk in pd.read_csv('train.csv', chunksize=chunksize):
    df= pd.DataFrame(chunk)
    break
