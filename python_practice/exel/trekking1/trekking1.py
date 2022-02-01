import xlrd

wb = xlrd.open_workbook('trekking1.xlsx')

sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])

dict = {}

for i in range(1, 38):
	row = sh.row_values(i, 0, 2)
	dict[row[0]] = row[1]

# print(dict)

sorted_dict = sorted(dict.items(), 
	key=lambda item: (-item[1], item[0]))
# print(sorted_dict)

for i, j in sorted_dict:
	print(i)