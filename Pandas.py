import pandas as pd

cols=['name','title','salary']
widths = [
    100, #name
    19, #title
    6, #salary
]


df=pd.read_fwf('fileWidthFile.txt',widths=widths,names=cols,delimeter=None)
print(df['title'])

import pandas as pd
import numpy as np

firstProductSet = pd.read_csv(r'C:\Users\Ron\Desktop\Test\File_1.csv')
df1 = pd.DataFrame(firstProductSet,columns= ['Product1', 'Price1'])

secondProductSet = pd.read_csv(r'C:\Users\Ron\Desktop\Test\File_2.csv')
df2 = pd.DataFrame(secondProductSet,columns= ['Product2', 'Price2'])

df1['Price2'] = df2['Price2']
df1['pricesMatch?'] = np.where(df1['Price1'] == df2['Price2'], 'True', 'False')
df1['priceDiff?'] = np.where(df1['Price1'] == df2['Price2'], 0, df1['Price1'] - df2['Price2'])

print (df1)

#https://stackoverflow.com/questions/41337316/pandas-compare-all-dataframe-columns-with-eachother
df_1.eq(df_2)
# .all returns True for a row if all values are True
df_1.eq(df_2).all(axis=1)
# .any returns true for row if any of the row's values are True
df_2[df_1.ne(df_2).any(axis=1)]

df_1.ne(df_3)

#Using Merge
# Need to rename Rings since we are merging on it but we want
# it to show as different columns post-merge
temp = df_new.rename({'Rings': 'Rings_new'}, axis=1)
merged = temp.merge(df_1, how='left',
                    left_on=['Player','Rings_new'],
                    right_on=['Player','Rings'])

#We can isolate out the new entries by slicing the dataframe for just the rows with a NaN value in Rings:
df_new[merged['Rings'].isna()]

#And concatenate to our dataframe like so:
final_df = pd.concat([df_1,
                      df_new[merged['Rings'].isna()]],
                     axis=0)