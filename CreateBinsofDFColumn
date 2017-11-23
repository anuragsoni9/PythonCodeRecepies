import numpy as np

df = pd.DataFrame({'value': np.random.randint(0, 100, 20)})

labels = [ "{0} - {1}".format(i, i + 9) for i in range(0, 100, 10) ]

df['group'] = pd.cut(df.value, range(0, 105, 10), right=False, labels=labels)

df.head(10)
