import pandas as pd

df = pd.read_excel("/Users/applemacintosh/Python/WITS/WITS_CHN_Tariff2018.xlsx", dtype='object')
df = pd.DataFrame(df)

First = df.pivot_table(index=['Doc_2018_No05+07_+25 percent since Aug 2018'], aggfunc='size')
First = pd.DataFrame(First)
First.columns = ['Doc_2018_No05+07_+25 percent since Aug 2018_N']
First.reset_index(inplace=True)
First["Doc_2018_No05+07_+25 percent since Aug 2018_tariff"] = 25
First["Doc_2018_No05+07_+25 percent since Aug 2018_sumtariff"] = First["Doc_2018_No05+07_+25 percent since Aug 2018_N"]*First["Doc_2018_No05+07_+25 percent since Aug 2018_tariff"]


merged_df = pd.merge(left=df, right=First, how='outer', left_on='Product_HS6', right_on='Doc_2018_No05+07_+25 percent since Aug 2018')


