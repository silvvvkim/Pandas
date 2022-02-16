import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
#®print(titanic)
df = titanic.loc[:, ['age','fare']]
print(df.tail())
print(type(df))
print('\n')

addition = df + 10
print(addition.tail())
print('\n')
print(type(addition))
print('\n')

substraction = addition - df
print(substraction.tail())
print('\n')
print(type(substraction))