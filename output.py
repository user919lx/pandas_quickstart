import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
df.to_excel('output/to_excel_1.xls')


df2 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
df2.to_excel('output/to_excel_2.xls', index=False)


df3 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
df3.to_excel('output/to_excel_3.xls', columns=['c', 'b'])