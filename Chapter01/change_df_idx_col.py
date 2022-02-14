import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index=['준서', '예은'], columns=['나이', '성별', '학교'])
print(df)
index = df.index
col = df.columns
print('\n')
print(index)
print('\n')
print(col)

df.index = ['학생 1', '학생 2']
df.columns = ['연령', '남녀', '소속']
print(df)