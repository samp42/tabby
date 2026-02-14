import tabby as tab
# import tabby.functions as fun

df1 = tab.read_csv("../../data/MOCK_DATA.csv")

df2 = df1.where(df1.age.gte(10) & df1.gender == "Male").select('*')

df2.show()

# df3 = df2.group_by(fun.split_text(df2.email, '.')[-1]).agg(
#     fun.count().as('domain_count')
# )
# df3.show()
