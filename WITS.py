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
merged_df["Doc_2018_No05+07_+25 percent since Aug 2018_average"] = merged_df["Doc_2018_No05+07_+25 percent since Aug 2018_sumtariff"]/merged_df['TotalTariffLines']

Second = df.pivot_table(index=['Doc_2018_No05+07_+25 percent since July 2018 (1)'], aggfunc='size')
Second = pd.DataFrame(Second)
Second.columns = ['Doc_2018_No05+07_+25 percent since July 2018 (1)_N']
Second.reset_index(inplace=True)
Second["Doc_2018_No05+07_+25 percent since July 2018 (1)_tariff"] = 25
Second["Doc_2018_No05+07_+25 percent since July 2018 (1)_sumtariff"] = Second["Doc_2018_No05+07_+25 percent since July 2018 (1)_N"]*Second["Doc_2018_No05+07_+25 percent since July 2018 (1)_tariff"]

merged_df = pd.merge(left=merged_df, right=Second, how='outer', left_on='Product_HS6', right_on='Doc_2018_No05+07_+25 percent since July 2018 (1)')
merged_df["Doc_2018_No05+07_+25 percent since July 2018 (1)_average"] = merged_df["Doc_2018_No05+07_+25 percent since July 2018 (1)_sumtariff"]/merged_df['TotalTariffLines']

Third = df.pivot_table(index=['Doc_2018_No06+No08_+5 percent (at the end) part 2 since Sep 2018'], aggfunc='size')
Third = pd.DataFrame(Third)
Third.columns = ['Doc_2018_No06+No08_+5 percent (at the end) part 2 since Sep 2018_N']
Third.reset_index(inplace=True)
Third["Doc_2018_No06+No08_+5 percent (at the end) part 2 since Sep 2018_tariff"] = 5
Third["Doc_2018_No06+No08_+5 percent (at the end) part 2 since Sep 2018_sumtariff"] = Third["Doc_2018_No06+No08_+5 percent (at the end) part 2 since Sep 2018_N"]*Third["Doc_2018_No06+No08_+5 percent (at the end) part 2 since Sep 2018_tariff"]

merged_df = pd.merge(left=merged_df, right=Third, how='outer', left_on='Product_HS6', right_on='Doc_2018_No06+No08_+5 percent (at the end) part 2 since Sep 2018')
merged_df["Doc_2018_No06+No08_+5 percent (at the end) part 2 since Sep 2018_average"] = merged_df["Doc_2018_No06+No08_+5 percent (at the end) part 2 since Sep 2018_sumtariff"]/merged_df['TotalTariffLines']

Fourth = df.pivot_table(index=['Doc_2018_No06+No08_+10 percent (at the end) since Sep 2018'], aggfunc='size')
Fourth = pd.DataFrame(Fourth)
Fourth.columns = ['Doc_2018_No06+No08_+10 percent (at the end) since Sep 2018_N']
Fourth.reset_index(inplace=True)
Fourth["Doc_2018_No06+No08_+10 percent (at the end) since Sep 2018_tariff"] = 10
Fourth["Doc_2018_No06+No08_+10 percent (at the end) since Sep 2018_sumtariff"] = Fourth["Doc_2018_No06+No08_+10 percent (at the end) since Sep 2018_N"]*Fourth["Doc_2018_No06+No08_+10 percent (at the end) since Sep 2018_tariff"]

merged_df = pd.merge(left=merged_df, right=Fourth, how='outer', left_on='Product_HS6', right_on='Doc_2018_No06+No08_+10 percent (at the end) since Sep 2018')
merged_df["Doc_2018_No06+No08_+10 percent (at the end) since Sep 2018_average"] = merged_df["Doc_2018_No06+No08_+10 percent (at the end) since Sep 2018_sumtariff"]/merged_df['TotalTariffLines']

Fifth = df.pivot_table(index=['Doc_2018_No06+No08_+20percent (at the end) part 2 since Sep 2018'], aggfunc='size')
Fifth = pd.DataFrame(Fifth)
Fifth.columns = ['Doc_2018_No06+No08_+20percent (at the end) part 2 since Sep 2018_N']
Fifth.reset_index(inplace=True)
Fifth["Doc_2018_No06+No08_+20percent (at the end) part 2 since Sep 2018_tariff"] = 20
Fifth["Doc_2018_No06+No08_+20percent (at the end) part 2 since Sep 2018_sumtariff"] = Fifth["Doc_2018_No06+No08_+20percent (at the end) part 2 since Sep 2018_N"]*Fifth["Doc_2018_No06+No08_+20percent (at the end) part 2 since Sep 2018_tariff"]

merged_df = pd.merge(left=merged_df, right=Fifth, how='outer', left_on='Product_HS6', right_on='Doc_2018_No06+No08_+20percent (at the end) part 2 since Sep 2018')
merged_df["Doc_2018_No06+No08_+20percent (at the end) part 2 since Sep 2018_average"] = merged_df["Doc_2018_No06+No08_+20percent (at the end) part 2 since Sep 2018_sumtariff"]/merged_df['TotalTariffLines']

Sixth = df.pivot_table(index=['Doc_2018_No06+No08_+25percent (at the end) since Sep 2018'], aggfunc='size')
Sixth = pd.DataFrame(Sixth)
Sixth.columns = ['Doc_2018_No06+No08_+25percent (at the end) since Sep 2018_N']
Sixth.reset_index(inplace=True)
Sixth["Doc_2018_No06+No08_+25percent (at the end) since Sep 2018_tariff"] = 25
Sixth["Doc_2018_No06+No08_+25percent (at the end) since Sep 2018_sumtariff"] = Sixth["Doc_2018_No06+No08_+25percent (at the end) since Sep 2018_N"]*Sixth["Doc_2018_No06+No08_+25percent (at the end) since Sep 2018_tariff"]

merged_df = pd.merge(left=merged_df, right=Sixth, how='outer', left_on='Product_HS6', right_on='Doc_2018_No06+No08_+25percent (at the end) since Sep 2018')
merged_df["Doc_2018_No06+No08_+25percent (at the end) since Sep 2018_average"] = merged_df["Doc_2018_No06+No08_+25percent (at the end) since Sep 2018_sumtariff"]/merged_df['TotalTariffLines']

Seventh = df.pivot_table(index=['Doc_2018_No10 + 2019_No01+No05+No07_stop + 5 percent from Jan 2019 to open end'], aggfunc='size')
Seventh = pd.DataFrame(Seventh)
Seventh.columns = ['Doc_2018_No10 + 2019_No01+No05+No07_stop + 5 percent from Jan 2019 to open end_N']
Seventh.reset_index(inplace=True)
Seventh["Doc_2018_No10 + 2019_No01+No05+No07_stop + 5 percent from Jan 2019 to open end_tariff"] = -5
Seventh["Doc_2018_No10 + 2019_No01+No05+No07_stop + 5 percent from Jan 2019 to open end_sumtariff"] = Seventh["Doc_2018_No10 + 2019_No01+No05+No07_stop + 5 percent from Jan 2019 to open end_N"]*Seventh["Doc_2018_No10 + 2019_No01+No05+No07_stop + 5 percent from Jan 2019 to open end_tariff"]

merged_df = pd.merge(left=merged_df, right=Seventh, how='outer', left_on='Product_HS6', right_on='Doc_2018_No10 + 2019_No01+No05+No07_stop + 5 percent from Jan 2019 to open end')
merged_df["Doc_2018_No10 + 2019_No01+No05+No07_stop + 5 percent from Jan 2019 to open end_average"] = merged_df["Doc_2018_No10 + 2019_No01+No05+No07_stop + 5 percent from Jan 2019 to open end_sumtariff"]/merged_df['TotalTariffLines']

Eighth = df.pivot_table(index=['Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 1) from Jan 2019 to open end (1)'], aggfunc='size')
Eighth = pd.DataFrame(Eighth)
Eighth.columns = ['Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 1) from Jan 2019 to open end (1)_N']
Eighth.reset_index(inplace=True)
Eighth["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 1) from Jan 2019 to open end (1)_tariff"] = -25
Eighth["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 1) from Jan 2019 to open end (1)_sumtariff"] = Eighth["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 1) from Jan 2019 to open end (1)_N"]*Eighth["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 1) from Jan 2019 to open end (1)_tariff"]

merged_df = pd.merge(left=merged_df, right=Eighth, how='outer', left_on='Product_HS6', right_on='Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 1) from Jan 2019 to open end (1)')
merged_df["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 1) from Jan 2019 to open end (1)_average"] = merged_df["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 1) from Jan 2019 to open end (1)_sumtariff"]/merged_df['TotalTariffLines']

Ninth = df.pivot_table(index=['Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 2) from Jan 2019 to open end'], aggfunc='size')
Ninth = pd.DataFrame(Ninth)
Ninth.columns = ['Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 2) from Jan 2019 to open end_N']
Ninth.reset_index(inplace=True)
Ninth["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 2) from Jan 2019 to open end_tariff"] = -25
Ninth["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 2) from Jan 2019 to open end_sumtariff"] = Ninth["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 2) from Jan 2019 to open end_N"]*Ninth["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 2) from Jan 2019 to open end_tariff"]

merged_df = pd.merge(left=merged_df, right=Ninth, how='outer', left_on='Product_HS6', right_on='Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 2) from Jan 2019 to open end')
merged_df["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 2) from Jan 2019 to open end_average"] = merged_df["Doc_2018_No10 + 2019_No01+No05+No07_stop + 25 percent (part 2) from Jan 2019 to open end_sumtariff"]/merged_df['TotalTariffLines']

Tenth = df.pivot_table(index=['Doc_2018_Other Series_No13_stop +15 percent since April 2018'], aggfunc='size')
Tenth = pd.DataFrame(Tenth)
Tenth.columns = ['Doc_2018_Other Series_No13_stop +15 percent since April 2018_N']
Tenth.reset_index(inplace=True)
Tenth["Doc_2018_Other Series_No13_stop +15 percent since April 2018_tariff"] = -15
Tenth["Doc_2018_Other Series_No13_stop +15 percent since April 2018_sumtariff"] = Tenth["Doc_2018_Other Series_No13_stop +15 percent since April 2018_N"]*Tenth["Doc_2018_Other Series_No13_stop +15 percent since April 2018_tariff"]

merged_df = pd.merge(left=merged_df, right=Tenth, how='outer', left_on='Product_HS6', right_on='Doc_2018_Other Series_No13_stop +15 percent since April 2018')
merged_df["Doc_2018_Other Series_No13_stop +15 percent since April 2018_average"] = merged_df["Doc_2018_Other Series_No13_stop +15 percent since April 2018_sumtariff"]/merged_df['TotalTariffLines']

Eleventh = df.pivot_table(index=['Doc_2018_Other Series_No13_stop +25 percent since April 2018'], aggfunc='size')
Eleventh = pd.DataFrame(Eleventh)
Eleventh.columns = ['Doc_2018_Other Series_No13_stop +25 percent since April 2018_N']
Eleventh.reset_index(inplace=True)
Eleventh["Doc_2018_Other Series_No13_stop +25 percent since April 2018_tariff"] = -25
Eleventh["Doc_2018_Other Series_No13_stop +25 percent since April 2018_sumtariff"] = Eleventh["Doc_2018_Other Series_No13_stop +25 percent since April 2018_N"]*Eleventh["Doc_2018_Other Series_No13_stop +25 percent since April 2018_tariff"]

merged_df = pd.merge(left=merged_df, right=Eleventh, how='outer', left_on='Product_HS6', right_on='Doc_2018_Other Series_No13_stop +25 percent since April 2018')
merged_df["Doc_2018_Other Series_No13_stop +25 percent since April 2018_average"] = merged_df["Doc_2018_Other Series_No13_stop +25 percent since April 2018_sumtariff"]/merged_df['TotalTariffLines']

Twelfth = df.pivot_table(index=['Doc_2019_No03_+5percent since June 2019'], aggfunc='size')
Twelfth = pd.DataFrame(Twelfth)
Twelfth.columns = ['Doc_2019_No03_+5percent since June 2019_N']
Twelfth.reset_index(inplace=True)
Twelfth["Doc_2019_No03_+5percent since June 2019_tariff"] = +5
Twelfth["Doc_2019_No03_+5percent since June 2019_sumtariff"] = Twelfth["Doc_2019_No03_+5percent since June 2019_N"]*Twelfth["Doc_2019_No03_+5percent since June 2019_tariff"]

merged_df = pd.merge(left=merged_df, right=Twelfth, how='outer', left_on='Product_HS6', right_on='Doc_2019_No03_+5percent since June 2019')
merged_df["Doc_2019_No03_+5percent since June 2019_average"] = merged_df["Doc_2019_No03_+5percent since June 2019_sumtariff"]/merged_df['TotalTariffLines']


