#! python3
# -*- codeing:utf-8 -*-

import openpyxl,sys,pprint,os

print('load file from excel...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_active_sheet()

print('calc data from workbook...')
countryData = {}
for i in range(2,sheet.max_row+1):
    state = sheet['B'+str(i)].value
    country = sheet['C'+str(i)].value
    pop = sheet['D'+str(i)].value

    countryData.setdefault(state,{})
    countryData[state].setdefault(country,{'tracts':0,'pop':0})
    countryData[state][country]['tracts'] += 1
    countryData[state][country]['pop'] += pop

print('Writing countryData to file...')
file = open('census2010.py','w')
file.write('allData = ' + pprint.pformat(countryData))
file.close()
print('Done.')
