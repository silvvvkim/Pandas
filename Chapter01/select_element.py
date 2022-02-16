import pandas as pd

exam_data = { '이름' : ['a','b','c'],
              '수학' : ['100','90', '80'],
              '영어' : ['100','90', '80'],
              '음악' : ['100','90', '80'],
              '체육' : ['100','90', '80']}

df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)
print(df)

a = df.loc['a','음악']
print(a)
print(df.iloc[0,2])
print(df.loc['a',['음악','체육']])
print(df.iloc[0,[2,3]])
print(df.iloc[0, 2:])
print(df.loc['a','음악':'체육'])