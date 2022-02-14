import pandas as pd

exam_data = { '이름' : ['a','b','c'],
              '수학' : ['100','90', '80'],
              '영어' : ['100','90', '80'],
              '음악' : ['100','90', '80'],
              '체육' : ['100','90', '80']}

df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')

math1 = df['수학']
print(math1)
print(type(math1))
print('\n')

eng = df.영어
print(eng)
print(type(eng))
print('\n')