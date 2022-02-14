import pandas as pd

exam_data = {'수학' : [90,80,70], '영어' : [90,80,70], '음악' : [90,80,70], '체육' : [90,80,70]}
df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

df2 = df[:]
df2.drop('서준', axis=0,inplace=True)
print(df2)
print('\n')

df3 = df[:]
print(id(df3))
print('\n')
df3 = df3.drop(['우현','인아'],axis=0)
print(df3)
print(id(df3))