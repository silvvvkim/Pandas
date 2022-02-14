import pandas as pd

exam_data = {'수학' : [90,80,70], '영어' : [90,80,70], '음악' : [90,80,70], '체육' : [90,80,70]}
df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1)
print(type(label1))
print('\n')

print(position1)
print(type(position1))
print('\n')

label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0,1]]
print(label2)
print(type(label2))
print('\n')

print(position2)
print(type(position2))
print('\n')

label3 = df.loc['서준' : '우현']
position3 = df.iloc[0 : 1]
print(label3)
print(type(label3))
print('\n')

print(position3)
print(type(position3))
print('\n')