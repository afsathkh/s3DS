import pandas as pd
details ={'name':['a','b','c','d'],
          'age':[24,25,26,27]}
df = pd.DataFrame(details)
print(df[:2])