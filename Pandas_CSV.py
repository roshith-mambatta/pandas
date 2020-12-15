import pandas as pd
import numpy as np

firstProductSet = pd.read_csv(r'test1.csv')
df1 = pd.DataFrame(firstProductSet, columns=['trade_id', 'trade_code', 'trade_schema', 'product'])
df1.set_index("trade_id", inplace=True)

secondProductSet = pd.read_csv(r'test2.csv')
df2 = pd.DataFrame(secondProductSet, columns=['trade_id', 'trade_code', 'trade_schema', 'product'])
df2.set_index("trade_id", inplace=True)

print(df1.eq(df2).all(axis=1))

print(df1.eq(df2))

df1 = df1.rename({'trade_code': 'trade_code1', 'trade_schema': 'trade_schema1', 'product': 'product1'}, axis=1)

merged = df1.merge(df2, how='left',
                   left_on=['trade_id'],
                   right_on=['trade_id'])

print(merged)
print(merged['trade_code'].isna())

####################### METHOD2 #####################################
firstProductSet = pd.read_csv(r'test1.csv')
df1 = pd.DataFrame(firstProductSet, columns=['trade_id', 'trade_code', 'trade_schema', 'product'])
df1.set_index("trade_id", inplace=True)

secondProductSet = pd.read_csv(r'test2.csv')
df2 = pd.DataFrame(secondProductSet, columns=['trade_id', 'trade_code', 'trade_schema', 'product'])
df2.set_index("trade_id", inplace=True)

# https://hackersandslackers.com/compare-rows-pandas-dataframes/
def dataframe_difference(df1: pd.DataFrame, df2: pd.DataFrame, df_key, which=None):
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(
        df2,
        indicator=True,
        how='outer',
        left_on=[df_key],
        right_on=[df_key]
    )
    if which is None:
        diff_df = comparison_df
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    #diff_df.to_csv('data/diff.csv')
    return diff_df


print(dataframe_difference(df1,df2,'trade_id','both'))
print(dataframe_difference(df1,df2,'trade_id','left_only'))
print(dataframe_difference(df1,df2,'trade_id','right_only'))

# how to make datetimes from unix epoch ints
# df['CreatedTimestamp'] = pd.to_datetime(df['CreatedDate'], unit='s')
# df['ModifiedTimestamp'] = pd.to_datetime(df['ModifiedDate'], unit='s')

