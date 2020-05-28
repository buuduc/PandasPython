from Excel import *
import pandas as pd
# Add du lieu vao code
BCC=ImportExcel("Bang-cham-cong-[5-2020].xlsx") #BCC la bang cham cong
Data=ImportExcel("FileThongtinnhanvien.xlsx")

# Tao 1 file excel dung de xuat du lieu
data=pd.DataFrame({'STT':[],'Vị trí CV':[],'Họ và Tên':[],'Ngày sinh':[],'Số điện thoại':[],'Tổng quân':[]})
demo=pd.ExcelWriter('Demo.xlsx',engine='xlsxwriter')
data.to_excel(demo,sheet_name='Công bố')
worksheet=demo.sheets['Công bố']
worksheet.conditional_format('A1:G1', {'type': '3_color_scale'})
workbook=demo.book
demo.save()

#
import CPU
CPU.ConvertData('05/05','FileThongtinnhanvien.xlsx','Bang-cham-cong-[5-2020].xlsx','vuiqua')
