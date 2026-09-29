
import pandas as pd
df = pd.DataFrame({
    'name': ['e', 'a', 'a', 'b', 'c', 'd'],
    'age': [1, 2, 1, 3, 4, 5],
    'rank': [0, 1, 2, 3, 4, 5]
})
print(df.to_string())
print('SORTED DATAFRAME')
df = df.sort_values(by=['name', 'age'], ascending=[True, True])
print(df.to_string())


