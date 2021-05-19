# HistoricReport.py
from datetime import date
from utils import DBUtils, DBQuerys, AppParams, AppUtils
import csv
import os

print("Init of Historic Report")

env='Test'

#Path Report folder
reportrep1Folder='{}Reportes{}{}\\'.format(AppParams.basePath, AppParams.rep1ReportType, env)
os.makedirs(reportrep1Folder, exist_ok=True)
reportrep2Folder='{}Reportes{}{}\\'.format(AppParams.basePath, AppParams.rep2ReportType, env)
os.makedirs(reportrep2Folder, exist_ok=True)

#Fecha actual
actualDate = date.today()

#Lista Años y Meses
yearLst = [actualDate.year-3, actualDate.year-2, actualDate.year-1, actualDate.year]
monthLst = [1,2,3,4,5,6,7,8,9,10,11,12]

for yearValue in yearLst:
        print('yearValue ', yearValue)
        yearrep1Folder='{}\\{}\\'.format(reportrep1Folder, yearValue)
        os.makedirs(yearrep1Folder, exist_ok=True)

        yearrep2Folder='{}\\{}\\'.format(reportrep2Folder, yearValue)
        os.makedirs(yearrep2Folder, exist_ok=True)

        for monthValue in monthLst:
                #Get Date Filters for Querys
                dateInit,dateEnd = AppUtils.getDateFilters(monthValue, yearValue)
                print('dateInit {} | dateEnd {}'.format(dateInit, dateEnd))

                #Execute rep1 report
                AppUtils.executeQueryReport(env, DBQuerys.queryReportrep1, dateInit, dateEnd, yearrep1Folder, AppParams.reportrep1Name, AppParams.rep1ColumnNames)
                #Execute rep2 report
                AppUtils.executeQueryReport(env, DBQuerys.queryReportrep2, dateInit, dateEnd, yearrep2Folder, AppParams.reportrep2Name, AppParams.rep2ColumnNames)

print("End of Historic Report")

#Unify rep1 report
AppUtils.unifiedReports(AppParams.basePath, AppParams.reportrep1Name ,AppParams.rep1ReportType, env, AppParams.rep1ColumnNames)
#Unify rep2 report
AppUtils.unifiedReports(AppParams.basePath, AppParams.reportrep2Name, AppParams.rep2ReportType, env, AppParams.rep2ColumnNames)
