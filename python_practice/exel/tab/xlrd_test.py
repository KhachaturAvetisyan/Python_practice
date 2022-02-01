import xlrd

wb = xlrd.open_workbook('tab.xlsx')

sheet_names = wb.sheet_names()
print(f"sheet_names = {sheet_names}")

sh = wb.sheet_by_name(sheet_names[0])
print(f"sh = {sh}")

nmin = sh.row_values(6)[2]
print(f"nmin = {nmin}")

for rownum in range(7, 27):
    temp = sh.row_values(rownum)
    print(f"temp = {temp}")

    nmin = min(nmin, temp[2])
    print(f"nmin = {nmin}")
    
print(nmin)