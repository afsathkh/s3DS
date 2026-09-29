import pandas as pd
data = { 'name':['e','a','a','b','c','d'],
         'age':[1,2,1,3,3,4],
         'rank':[0,1,2,3,4,5]}
df = pd.DataFrame(data, index=['a1','b1','c1','d1','e1','f1'])
print(df.to_string())
df.reset_index(inplace=True,drop=True)
print(df.to_string())