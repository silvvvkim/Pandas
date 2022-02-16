import pandas as pd

dict_data = { 'c0' : [1,2,3], 'c1' : [1,2,3], 'c2' : [1,2,3], 'c3' : [1,2,3],'c4' : [1,2,3] }

df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df)

df2 = df.reindex(['r0','r1','r2','r3','r4'])
print(df2)

df3 = df.reindex(['r0','r1','r2','r3','r4'], fill_value=0)
print(df3)