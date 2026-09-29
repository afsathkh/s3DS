import pandas as pd
import numpy as np
nums = {'set_of_numbers':[2,3,5,7,11,13,np.nan,19,23,np.nan]}
df = pd.DataFrame(nums,columns=["set_of_numbers"])
df['set_of_numbers']= df['set_of_numbers']
df['set_of_numbers']=df['set_of_numbers'].fillna(0)
print(df)