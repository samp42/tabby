import tabby as tab

df1 = tab.read_csv("path")

df2 = df1.where(df1.col1.gte(10) & df1.col2.eq('my_text')).select('*')

df3 = tab.from_db('')
