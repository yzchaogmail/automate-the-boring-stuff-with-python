import sys,os
import openpyxl as excel
#os.getcwd()
#print(os.getcwd())
path = os.chdir(os.getcwd())
print(os.getcwd())
try:
    workbook = excel.load_workbook('example.xlsx')
    print('Success load workbook "example.xlsx"')
    print(workbook.get_sheet_names())
    #print(os.getcwd())
except:
    print('Failed to load workbook "example.xlsx"')
