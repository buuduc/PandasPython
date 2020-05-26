import pandas as pd
import numpy as np
from Excel import *
import TableConfig
day='05/05'
data=pd.DataFrame(ImportExcel("Bang-cham-cong-[5-2020].xlsx"))
ThongTin=pd.DataFrame(ImportExcel("FileThongtinnhanvien.xlsx"))
id=TableConfig.GetColumn(data,0,day)
# l=data.iloc[:,index]
ThongTin.columns=ThongTin.iloc[0]
k=ThongTin.iloc[1:len(ThongTin),2]
l=list(set(k))
# for i in l:
# for i in range(len(data)):
#     if data[data.iloc[]]
# ThongTin.columns==ThongTin.iloc[0]
datafr=pd.DataFrame()
for i in range(len(l)):
    kk=ThongTin.where(ThongTin.iloc[1:len(data),2]==l[i]).dropna()
    for j in range(len(kk)):
        if len(data[data.index==kk.index[j]])>0:
            if (data.loc[kk.index[j]].iloc[id]!='x' or data.loc[kk.index[j]].iloc[id]!=''):
                datafr = datafr.append(kk.iloc[j])
                print(data.loc[kk.index[j]].iloc[id])
ExportExcel('dd',datafr)
# df1.append(df2, ignore_index = True)
# K=data.loc['DH0158'].iloc[id]

