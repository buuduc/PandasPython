import pandas as pd


def ImportExcel(Path):
    try:
        a = pd.read_excel(Path, sheet_name=0, index_col=0)
        return a
    except:
        return 0

def ExportExcel(Name,SheetName,Data):
    # try:
    demo = pd.ExcelWriter(Name, engine='xlsxwriter')
    Data.to_excel(demo, sheet_name=SheetName)
    # workbook = demo.book
    # format = workbook.add_format()
    # format.set_align('center')
    # format.set_align('vcenter')
    # worksheet=demo.sheets[SheetName]
    # worksheet.
    worksheet = demo.sheets[SheetName]  # pull worksheet object
    for idx, col in enumerate(Data):  # loop through all columns
        series = Data[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
        )) + 1  # adding a little extra space
        worksheet.set_column(idx, idx, max_len)  # set column width

    demo.save()
    return 1
    # except:
    #     return 0
