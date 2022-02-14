import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17 , '여', '수리중']], index=['준서', '예은'], columns=['나이', '성별', '학교'])
print(df)
print('\n')
print("id : ", id(df))
df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True)
df.rename(index={'준서':'학생 1', '예은':'학생 2'},inplace=True)
print(df)
print("id : ", id(df))