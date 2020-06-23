'''
Join two dataframes

Joins on index, otherwise use on='$COLUMN'

Types:
left, right, outer, inner
'''

df_joint = df1.join(df2, how='$TYPE')
