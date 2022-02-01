import xlrd
import math 

wb = xlrd.open_workbook('trekking2.xlsx')

sheet_names = wb.sheet_names()
# print(sheet_names)

handbook = wb.sheet_by_name(sheet_names[0])

dict = {}

for i in range(1, 38):
	row = handbook.row_values(i, 0, 5)

	# print(row)

	for i in range(len(row)):
		if row[i] == '':
			row[i] = 0;

	dict[row[0]] = [row[1], row[2], row[3], row[4]]

# print(dict)

layout = wb.sheet_by_name(sheet_names[1])

sum_kkal = 0
sum_b = 0
sum_j = 0
sum_u = 0

for i in range(1, 13):
	row = layout.row_values(i)
	# print(row)
	all_stat = dict[row[0]]
	kkal = (row[1] * all_stat[0]) / 100
	b = (row[1] * all_stat[1]) / 100
	j = (row[1] * all_stat[2]) / 100
	u = (row[1] * all_stat[3]) / 100

	sum_kkal += kkal
	sum_b += b
	sum_j += j
	sum_u += u

print(math.floor(sum_kkal), 
	math.floor(sum_b), 
	math.floor(sum_j), 
	math.floor(sum_u))