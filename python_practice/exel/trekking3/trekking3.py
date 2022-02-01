import xlrd
import math
import pdb


wb = xlrd.open_workbook('trekking3.xlsx')

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
sum_kkal = sum_b = sum_j = sum_u = 0

day = last_day = 1

# pdb.set_trace()
for i in range(1, 100):
	row = layout.row_values(i)

	all_stat = dict[row[1]]

	kkal = (row[2] * all_stat[0]) / 100
	b = (row[2] * all_stat[1]) / 100
	j = (row[2] * all_stat[2]) / 100
	u = (row[2] * all_stat[3]) / 100

	last_day = day
	day = row[0]
	

	if day != last_day:
		print(" ".join(list(map(
			lambda x: str(math.floor(x)),
		 	[sum_kkal, sum_b, sum_j, sum_u]))))
		sum_kkal = sum_b = sum_j = sum_u = 0
		
	sum_kkal += kkal
	sum_b += b
	sum_j += j
	sum_u += u

	# if day == 9:
	# 	# print(row)
	# 	print(kkal, b, j, u)
	# 	print(day, last_day)
		# print(sum_kkal, sum_b, sum_j, sum_u)


print(" ".join(list(map(
	lambda x: str(math.floor(x)),
 	[sum_kkal, sum_b, sum_j, sum_u]))))
