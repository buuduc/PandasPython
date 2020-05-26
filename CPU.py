import pandas as pd
import numpy as np
from Excel import ImportExcel
import TableConfig
day='05/05'
data=pd.DataFrame(ImportExcel("Bang-cham-cong-[5-2020].xlsx"))
index=TableConfig.GetColumn(data,0,day)
l=data.iloc[:,index]



