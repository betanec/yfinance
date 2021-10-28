import pandas as pd
from pandas.core.reshape.concat import concat
import yfinance as yf
import xlrd

def export_data():
    rb = xlrd.open_workbook('C:\it\way\list_curr.xls', formatting_info=True)
    tikers = [x for xs in [rb.sheet_by_index(0).row_values(rownum) for rownum in range(378)] for x in xs]
    print(tikers)
    dwnl_count = 2 # len(tikers)
    union = pd.concat([pd.DataFrame(yf.download(tikers[i], period = '2d', interval = '15m')) for i in range(dwnl_count)])
    print(union)
    union.to_csv('data1.csv')
    
export_data()