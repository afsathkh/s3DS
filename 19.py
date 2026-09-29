import pandas as pd
details = {
    'name':['a','b','c','d','e'],
    'occupation':['a1','a1','a1','b1','b1'],
    'salary':[20,30,40,27,23]
}
df = pd.DataFrame(details)
print(df)
occ_average_age = df.groupby('occupation')['salary'].mean()
print("Average salary per occupation:")
print(occ_average_age)