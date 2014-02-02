#import data from worksheets
#xlrd package needs to be downloaded
#function takes in document name (looking to eventual steps towards gui)
#data is scanned into 2D list, first item of each list is the title of the column

def scan(name):
	import xlrd
	workbook=xlrd.open_workbook(name)
	sheet=workbook.sheet_by_name(workbook.sheet_names()[0])
	num_rows=sheet.nrows
	num_cells=sheet.ncols
	data=[[] for i in range(num_cells-1)]
	for curr_cell in range(num_cells-1):
		temp=[]
		for curr_row in range (num_rows-1):
			temp.append(sheet.cell_value(curr_row,curr_cell))
		data[curr_cell]=temp	
	return(data)
