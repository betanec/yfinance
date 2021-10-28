import pandas as pd
import yfinance as yf
import xlrd



rb = xlrd.open_workbook('C:\it\way\list_curr.xls', formatting_info=True)
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(380)]
tikers = [x for xs in vals for x in xs]


def export_data(i):
    data = yf.download(tikers[i], period = '2d', interval = '15m')
    df = pd.DataFrame(data)
    df.to_csv(str(tikers[i]) + '.csv') 


def counting(): 
    schetchick1 = 0
    while schetchick1 != len(tikers):
        export_data(schetchick1)
        schetchick1 += 1
counting()
# говно для того чтобы сразу была сборка csv внутри PBI