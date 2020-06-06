import pandas as pd
import numpy as np
from Excel_usable import ImportExcel
import TableConfig
day='05/05'
data=pd.DataFrame(ImportExcel("Bang-cham-cong-[5-2020].xlsx"))
ThongTin=pd.DataFrame(ImportExcel("FileThongtinnhanvien.xlsx"))
daythutu=TableConfig.GetColumn(data,0,day)
# l=data.iloc[:,index]
datafr=pd.DataFrame({'STT':[],'Vị trí CV':[],'Họ và Tên':[],'Ngày sinh':[],'Số điện thoại':[],'Tổng quân':[]})
k=ThongTin.iloc[1:len(ThongTin),2]
l=pd.DataFrame(set(k))
cnt=0
for i in l:
    datafr.append(l)
    # for i in range(data):
    print(i)
# DH0158
data.loc['DH0158'].iloc[2]