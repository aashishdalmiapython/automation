import xlwt # import excelwrite module

# create Workbook class object
objworkbook= xlwt.Workbook()
# create sheet object
wsheet = objworkbook.add_sheet("Test Result")
# write to the sheet cell
wsheet.write(0,0,"TC1")
wsheet.write(0,1,"Pass")

# save the file
objworkbook.save("C:\FileRead\XLRD_write.xls")

### Note - dont create file in xlsx format, its not supported by xlwt module