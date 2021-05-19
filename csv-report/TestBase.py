from datetime import date
from utils import AppUtils, DBQuerys, AppParams, DBUtils



print('Init of Test Base')

env='Test'

#FechaActual
actualDate = date.today()

iniFilter,endFilter = AppUtils.getDateFilters(actualDate.month, actualDate.year)

print('Test result. ini date: {} | end date {}'.format(iniFilter, endFilter))

print(DBQuerys.queryReportrep1.format(iniFilter, endFilter))

connection = DBUtils.getDbConnection(env)
cursor = connection.cursor()
cursor.execute(DBQuerys.queryTest)

AppUtils.writeCsvReportFile(AppParams.basePath, AppParams.reportrep2Name, iniFilter, cursor, AppParams.columnNames)

connection.close()

print('End of Test Base')