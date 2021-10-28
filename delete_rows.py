import xlrd
import csv
import os
import pandas as pd

rb = xlrd.open_workbook('C:\it\way\list_curr.xls', formatting_info=True)
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(380)]
tikers = [x for xs in vals for x in xs]
print(tikers)

def new_csv():
    for i in tikers:
        next_name_file = "".join(i + '.csv')
        with open(os.path.join('C:\it', next_name_file)) as inp:
            row_count = sum(1 for check in csv.reader(open(next_name_file,"r+")))
            print(row_count)
            df = pd.DataFrame(inp)
            df.drop(df.index[[x for x in range(2,row_count-1)]], inplace=True)
            df.to_csv(str(i) + '_edited.csv')
new_csv()
# ридер просто урезанная версия без фичи с delete

