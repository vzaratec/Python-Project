from utils import DBUtils
import csv
import os

# Method obtaind date filters to execute querys
def getDateFilters(monthValue, yearValue):
    print('Get Date Filters')
    monthInit = '{}'.format(monthValue)
    monthEnd = '{}'.format(monthValue+1)
    yearInit = yearValue
    yearEnd = yearValue
    if monthValue == 12:
        monthInit = '{}'.format(monthValue)
        monthEnd = '01'
        yearEnd = yearInit + 1
    if len(str(monthInit)) == 1:
        monthInit = '0{}'.format(monthInit)
    if len(str(monthEnd)) == 1:
        monthEnd = '0{}'.format(monthEnd)

    dateInit = '{}/{}'.format(monthInit,yearInit)
    dateEnd = '{}/{}'.format(monthEnd,yearEnd)

    return dateInit, dateEnd

# Method execute query and generate report files
def executeQueryReport(environment, query, dateInit, dateEnd, folderPath, reportName, columnNames):
    try:
        # Connection to database
        connection = DBUtils.getDbConnection(environment)
        cursor = connection.cursor()
        print('Inicia ejecucion query')
        cursor.execute(query.format(dateInit, dateEnd))
        print('Finaliza ejecucion query')

        print('Inicia escritura archivo')
        writeCsvReportFile(folderPath, reportName, dateInit, cursor, columnNames)
        print('Fin escritura archivo')
        connection.close()
    except Exception as e:
        print('An exception occurred: ', e) 

# Method write a physical report in csv file
def writeCsvReportFile(folderPath, reportName, dateInit, cursor, columnNames):
    fileName ='{}{}{}.csv'.format(folderPath, reportName, dateInit.replace('/',"-"))
    reportFile = open(fileName, 'w')

    myFile = csv.writer(reportFile, lineterminator = '\n')
    myFile.writerow(columnNames)

    for rows in cursor:
        #print('rows => {}'.format(rows[0]))
        myFile.writerow(rows)
        
    reportFile.close()


# Method unified monthly reports to a annual report
def unifiedReports(basePath, testReportName, reportType, environment, columnNames):
    #carpeta donde se encuentran los reportes a unificar
    reportFolder='{}Reportes{}{}\\'.format(basePath, reportType, environment)

    print('Main Report Folder Path => ' + reportFolder)
    try:
        with os.scandir(reportFolder) as directory:
            for reportDir in directory:
                if(reportDir.is_dir()):
                    print('Report Directory => ' + reportDir.name)
                    unifiedReportName ='{}{}_{}.csv'.format(reportFolder, testReportName, reportDir.name)
                    print('Unified Report Name => ' + unifiedReportName)
                    unifiedReportPath = open(unifiedReportName, 'w')
                    unifiedReport = csv.writer(unifiedReportPath, lineterminator = '\n')
                    unifiedReport.writerow(columnNames)
                    subfolderPath = '{}{}'.format(reportFolder, reportDir.name)
                    #print('subfolderPath => ' + subfolderPath)

                    with os.scandir(subfolderPath) as subfolder:
                        for reportFile in subfolder:
                            print('Reading Report File => ' + reportFile.name)
                            reportName = '{}\\{}'.format(subfolderPath, reportFile.name)
                            with open(reportName , newline='') as csvReport:
                                csvReport.readline()
                                reader = csv.reader(csvReport)
                                for row in reader:
                                    #print(row)
                                    unifiedReport.writerow(row)
                                csvReport.close()
                                #print('Closing Report File')
                    print('Closing Unified Report File')
                    unifiedReportPath.close()
    except Exception as e:
        print('An exception occurred: ', e) 
