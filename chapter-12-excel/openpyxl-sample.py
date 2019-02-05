import sys,os
import openpyxl as excel
#os.getcwd()
#print(os.getcwd())
#path = os.chdir(os.getcwd())
print(os.getcwd())

try:
    workbook = excel.load_workbook('example.xlsx')
    print('Success load workbook "example.xlsx"')
    print(workbook.get_sheet_names())
    #print(os.getcwd())
    '''
    try:
        sheet = workbook.get_sheet_by_name('Sheet3')
        # print(type(sheet))
        print('get_sheet_by_name Sheet-title:%s' %sheet.title)
    except:
        print('Failed to get sheet by name.')
    '''
    sheet = workbook.get_active_sheet()
    print(sheet['A1'].value)
    print(sheet['B1'].value)
    cell = sheet['B1']
    print(cell.row)
    print(cell.column)
    print(cell.coordinate)
    for i in range(1,8,2):
        cell = sheet.cell(row = i,column=2)
        print(i,cell.row,cell.column,cell.value)
except:
    print('Failed to load workbook "example.xlsx"')
