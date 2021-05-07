# PresentReport.py
from datetime import date
from utils import DBUtils, DBQuerys, AppParams, AppUtils
import csv
import os

print("Init of Present Year Report")

env='Test'

#FechaActual
actualDate = date.today()
#Lista Años y Meses
monthLst = [1,2,3,4,5,6,7,8,9,10,11,12]

#Path Report folder
reportrep1Folder='{}Reportes{}{}\\{}\\'.format(AppParams.basePath, AppParams.rep1ReportType, env, actualDate.year)
os.makedirs(reportrep1Folder, exist_ok=True)
reportrep2Folder='{}Reportes{}{}\\{}\\'.format(AppParams.basePath, AppParams.rep2ReportType, env, actualDate.year)
os.makedirs(reportrep2Folder, exist_ok=True)

for monthValue in monthLst:
        #Get Date Filters for Querys
        dateInit,dateEnd = AppUtils.getDateFilters(monthValue, actualDate.year)
        print('dateInit {} | dateEnd {}'.format(dateInit, dateEnd))

        #Execute rep1 report
        AppUtils.executeQueryReport(env, DBQuerys.queryReportrep1, dateInit, dateEnd, reportrep1Folder, AppParams.reportrep1Name, AppParams.rep1ColumnNames)
        #Unify rep1 report
        AppUtils.unifiedReports(AppParams.basePath, AppParams.reportrep1Name, AppParams.rep1ReportType, env, AppParams.rep1ColumnNames)
        
        #Execute rep2 report
        AppUtils.executeQueryReport(env, DBQuerys.queryReportrep2, dateInit, dateEnd, reportrep2Folder, AppParams.reportrep2Name, AppParams.rep2ColumnNames)
        #Unify rep2 report
        AppUtils.unifiedReports(AppParams.basePath, AppParams.reportrep2Name, AppParams.rep2ReportType, env, AppParams.rep2ColumnNames)


print("End of Present Year Report")