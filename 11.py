from operator import index

import pandas as pd
sr=pd.Series(pd.date_range('2021-05-01','2021-05-21',freq='D'))
print(sr.to_string(index=False))