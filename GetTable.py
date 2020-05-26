import pandas as pd
import numpy as np
from Excel import ImportExcel


def GetColumn(data, row, value):
    return np.where(data.iloc[0, :].values == value)[row][0]
