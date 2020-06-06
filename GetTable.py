import pandas as pd
import numpy as np
from Excel_usable import ImportExcel


def GetColumn(data, row, value):
    return np.where(data.iloc[0, :].values == value)[row][0]
