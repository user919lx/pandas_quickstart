import pandas as pd

# ================= 读取数据 =================
# ----------------- excel --------------------
# 基础用法
df = pd.read_excel('data/read_excel.xlsx')
print(df)

# 设定要读取的表
df2 = pd.read_excel('data/read_excel.xlsx',sheetname='Sheet2')
print(df2)

# 设定跳过行
df3 = pd.read_excel('data/read_excel.xlsx', skiprows=[0, 4])
print(df3)


# - csv/txt-
# csv
df4 = pd.read_csv('data/read_csv.csv')
print(df4)

# txt
df5 = pd.read_csv('data/read_table.txt', sep='|')
print(df5)

# # -------------------- sql --------------------
# # 基础用法
# username = 'root'
# password = 'root'
# database = 'pandas'
#
# sql_uri = 'mysql://'+username+':'+password+'@localhost:3306/'+database
# df4 = pd.read_sql("data", sql_uri)
# print(df4)

