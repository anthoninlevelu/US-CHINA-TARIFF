import pandas as pd
df = pd.read_excel("/Users/applemacintosh/Python/WITS/WITS_CHN_Tariff2018.xlsx")
df = pd.DataFrame(df)
df['Product_HS6'] = df['Product_HS6'].map(lambda x: f'{x:0>6}')

Doc_2018_No05_07 = df.pivot_table(index=['Doc_2018_No05+07_+25 percent since Aug 2018'], aggfunc='size')
Doc_2018_No05_07 = pd.DataFrame(Doc_2018_No05_07)
Doc_2018_No05_07.columns = ['Doc_2018_No05_07_N']
Doc_2018_No05_07.reset_index(inplace=True)
Doc_2018_No05_07 = Doc_2018_No05_07.rename(columns={'Doc_2018_No05+07_+25 percent since Aug 2018': 'Doc_2018_No05_07'})
Doc_2018_No05_07["Doc_2018_No05_07_+tariff"] = 25
Doc_2018_No05_07["Doc_2018_No05_07_sumtariff"] = Doc_2018_No05_07["Doc_2018_No05_07_N"]*Doc_2018_No05_07["Doc_2018_No05_07_+tariff"]

Doc_2018_No05_07 = Doc_2018_No05_07.astype(int)
df['Product_HS6'] = df['Product_HS6'].astype(int)

merged_df= pd.merge(left=df, right=Doc_2018_No05_07, how='outer', left_on='Product_HS6', right_on='Doc_2018_No05_07')
merged_df[]


