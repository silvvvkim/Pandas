import pandas as pd

exam_data = {'수학' : [90,80,70], '영어' : [90,80,70], '음악' : [90,80,70], '체육' : [90,80,70]}
df = pd.DataFrame(exam_data, index=['a','b','c'])
print('id : ', id(df))
print(df)
print('\n')

df2 = df[:]
df2.drop(['수학','영어'],axis=1,inplace=True)
print('id : ', id(df2))
print(df2)
print('\n')

df3 = df[:]
df3 = df3.drop('체육', axis=1)
print('id : ', id(df3))
print(df3)
print('\n')
