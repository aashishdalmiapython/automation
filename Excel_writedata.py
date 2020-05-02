import xlwt

objworkbook= xlwt.Workbook()
wsheet = objworkbook.add_sheet("Test Result")
wsheet.write(0,0,"TC1")
wsheet.write(0,1,"Pass")
### Note - dont create file in xlsx format, its not supported by xlwt module
objworkbook.save("C:\FileRead\XLRD_write.xls")