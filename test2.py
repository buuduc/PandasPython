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
# l=['Phòng Kế Toán', 'CÔNG TY TNHH KỸ THUẬT THƯƠNG MẠI VÀ DỊCH VỤ DOCTOR HOUSE', 'Công trình xưởng Ricons Giai Đoạn 2', 'Phòng CCM', 'Công trình xưởng BW Bàu Bàng - Bình Dương', 'Công trình Brotex - Tây Ninh', 'Công trình WATERBAY - HCM', 'Công trình Paiho - HCM', 'Giám Đốc', 'Phòng Vật Tư Thiết Bị', 'Công trình Avani - Vũng Tàu', 'Phòng Kỹ Thuật', 'Công trình Apec Wynham Phú Yên', 'Công trình SwanBay Nhơn Trạch', 'Lee House', 'Công trình', 'Công trình Swan Park - Nhơn Trạch', 'Công trình VINCITY - Gia Lâm', 'Phòng Tổng Hợp', 'Công trình AQUABAY - Hưng Yên', 'Công trình Đại Quang Minh - HCM', 'Phòng Quản Lý Tài Sản', 'Công trình Worldon - Củ Chi', 'Mars House']


# for i in l:
# for i in range(len(data)):
#     if data[data.iloc[]]
# ThongTin.columns==ThongTin.iloc[0]
datafr=pd.DataFrame()
# datafr['Tên','Vị trí','Công trình','Ngày sinh','Sđt','Tổng quân']=''
datafr['Tổng quân']=''
datafr['STT']=''
check=True
# sodem=[]
Lct=[]
stt=0
for i in range(len(l)):
    sodem = 0
    kk=ThongTin.where(ThongTin.iloc[1:len(data),2]==l[i]).dropna()
    for j in range(len(kk)):
        if len(data[data.index==kk.index[j]])>0:

            if (data.loc[kk.index[j]].iloc[id]!='x' and pd.isna(data.loc[kk.index[j]].iloc[id])==False):
                sodem+=1
                datafr = datafr.append(kk.iloc[j])
                stt+=1
                datafr.loc[kk.index[j], 'STT'] = stt
                if check:
                    Lct.append(kk.index[j])
                    locate=j
                    check=not check

                # print(data.loc[kk.index[j]].iloc[id])
        # test=kk.where(kk.index[locate]).dropna()
        if j == (len(kk) - 1) and len(kk)>0 and sodem!=0:
            datafr.loc[Lct[len(Lct)-1], 'Tổng quân'] = sodem



    check=True
datafr=datafr[['STT','Tên','Vị trí','Công trình','Ngày sinh','Sđt','Tổng quân']]
ExportExcel('dd',datafr)
# df1.append(df2, ignore_index = True)
# K=data.loc['DH0158'].iloc[id]