import pandas as pd


def ImportExcel(Path):
    try:
        a = pd.read_excel(Path, sheet_name=0, index_col=0)
        return a
    except:
        return 0

def ExportExcel(Name,Data):
    try:
        demo = pd.ExcelWriter(Name+'.xlsx', engine='xlsxwriter')
        Data.to_excel(demo, sheet_name='Công bố')
        demo.save()
        return 1
    except:
        return 0
