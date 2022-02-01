import xlrd

wb = xlrd.open_workbook('salaries.xlsx')

sheet_names = wb.sheet_names()
# print(f"sheet_names = {sheet_names}")

sh = wb.sheet_by_name(sheet_names[0])
# print(f"sh = {sh}")

dict = {}

for i in range(1, 9):
	rows = sh.row_values(i, 1, 8)
	rows.sort()
	median = rows[3]

	city = sh.row_values(i)[0]

	dict[median] = city

# for i in dict:
# 	print(i, dict[i])

all_median = list(dict.keys())
# print(all_median)
all_median.sort()
# print(all_median)
max_median = all_median[-1]
max_median_city = dict[max_median]
# print(f"{max_median_city} - {max_median}")


dict = {}

for i in range(1, 8):
	colmns = sh.col_values(i, 1, 9)
	# print(colmns)
	colmns_min = sum(colmns) / 8
	# print(colmns_min)

	prof = sh.col_values(i)[0]
	# print(prof)

	dict[colmns_min] = prof

all_min = list(dict.keys())
all_min.sort()
max_min = all_min[-1]
max_min_prof = dict[max_min]
# print(f"{max_min_prof} - {max_min}")

print(max_median_city, max_min_prof)