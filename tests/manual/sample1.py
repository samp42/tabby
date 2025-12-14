import tabby as tab

df1 = tab.read_csv("path")

df2 = df1.where(df1.col1.gte(10) & df1.col2.eq('my_text')).select('*')

df3 = tab.from_db('')

df4 = df2.join(df3, on='id', how='left_anti')

"""
df1 <- CSV_SCAN "file.csv"
df2 <- FILTER & (>= col1 10) (== col2 'my_text')
df3 <- DB_SCAN SQL `sql query`
df4 <- JOIN df2 df3, id, LEFT ANTI
"""
