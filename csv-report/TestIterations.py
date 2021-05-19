# TestIterations.py
from datetime import date
from utils import AppParams
import csv
import os

print("Init of TestIterations")

path='%REPORT_PATH%'

env='Test'

#actual date
actualDate = date.today()

#years list
yearLst = [actualDate.year-3, actualDate.year-2, actualDate.year-1, actualDate.year]
monthLst = [1,2,3,4,5,6,7,8,9,10,11,12]

reportFolder='{}Reportes{}\\'.format(path, env)
os.makedirs(reportFolder, exist_ok=True)

print('reportFolder {}'.format(reportFolder))
for yearValue in yearLst:
        print('yearValue ', yearValue)
        yearFolder='{}\\{}\\'.format(reportFolder, yearValue)
        os.makedirs(yearFolder, exist_ok=True)
        for monthNmb in monthLst:
            #Get Date Filters for Querys
            dateInit,dateEnd = AppUtils.getDateFilters(monthNmb, yearValue)
            print('dateInit {} | dateEnd {}'.format(dateInit, dateEnd))
            
            result = """ FCH >= TO_DATE('{}', 'MM/YYYY') AND FCH <  TO_DATE('{}', 'MM/YYYY') """.format(dateInit,dateEnd)
            
            fileName ='{}Report_{}.csv'.format(yearFolder, dateInit.replace('/',"-"))
            fp = open(fileName, 'w')

            myFile = csv.writer(fp, lineterminator = '\n')
            myFile.writerow(AppParams.rep1ColumnNames)
            myFile.writerow(result)
            fp.close()

print("End of TestIterations")