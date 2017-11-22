import os
import pandas as pd

#get strucutre of csv file by reading 1 row and deletting data from it
chunksize = 1
for chunk in pd.read_csv('train.csv', chunksize=chunksize):
    df= pd.DataFrame(chunk)
    break

df=df.drop(df.index[[0]])


# Now, reading all rows in chunks
chunksize = 100000

for chunk in pd.read_csv('train.csv', chunksize=chunksize):
    df= pd.DataFrame(chunk)
    

    
