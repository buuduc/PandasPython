import pandas as pd
import numpy as np
from Excel import ImportExcel
data=pd.DataFrame(ImportExcel("Bang-cham-cong-[5-2020].xlsx"))
# print(data.iloc[[:,[1,data.iloc]])
# da=data.where(data.iloc[:,7]=='x')
da=data.iloc[0,7]
print(data.iloc[0,5])
np.where(data.iloc[0,:].values=='05/05')
# id=data.first_valid_index(data.iloc[2,:]=="05/05")
# id=data.first_valid_index()
# data.to_excel('test.xlsx',sheet_name='Công bố')
print(da)

