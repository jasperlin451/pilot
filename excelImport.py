def scan(name):
	import xlrd
	workbook=xlrd.open_workbook(name)
	sheet=workbook.sheet_by_name('Sheet1')
	return(sheet.cell_value(5,5))
