import xlrd # import xlrd module/package

objworkbook = xlrd.open_workbook("C:/FileRead/XLRD.xls") # create workbook object
# use nsheets(variable) to check no of sheets available in the workbook
Noofsheets = objworkbook.nsheets
print("no of sheets are" , Noofsheets)
# move to the sheet level either using sheet_by_index/sheet_by_name
Worksheet = objworkbook.sheet_by_index(0)
print("Selected the first worksheet" , Worksheet)
no_of_column = Worksheet.ncols
no_of_rows = Worksheet.nrows
print(no_of_column)
print(no_of_rows)

# move to the column level
cell_value = Worksheet.cell(1,1).value
print(cell_value)

# loop to get all the values from worksheet column & rows
for row in range(no_of_rows):
    for colm in range(no_of_column):
        value = Worksheet.cell(row,colm).value
        print("Value @ (" + str(row) + "," +str(colm)+") Is = " + value) # Value @ (0,0) Is = Data1

