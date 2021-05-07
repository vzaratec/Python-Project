
class AppParams :

    def appParams(self):
        #db
        self.dbUser = dbUser
        self.dbPass = dbPass
        self.dbHostAmb1 = dbHostAmb1
        self.dbPortAmb1 = dbPortAmb1
        self.dbSvcNameAmb1 = dbSvcNameAmb1
        self.dbHostAmb2 = dbHostAmb2
        self.dbPortAmb2 = dbPortAmb2
        self.dbSvcNameAmb2 = dbSvcNameAmb2
        #app
        self.basePath = basePath
        self.rep1ColumnNames = rep1ColumnNames
        self.reportrep1Name = reportrep1Name
        self.rep1ReportType = rep1ReportType
        self.rep2ColumnNames = rep2ColumnNames
        self.reportrep2Name = reportrep2Name
        self.rep2ReportType = rep2ReportType


#db
dbUser = 'dbUserValue'
dbPass = 'dbPassValue'
dbHostAmb1 = 'hostValue'
dbPortAmb1 = 'portValue'
dbSvcNameAmb1 = 'instanceValue'
dbHostAmb2 = 'hostValue'
dbPortAmb2 = 'portValue'
dbSvcNameAmb2 = 'instanceValue'
#app
basePath='%REPORT_PATH%'
rep1ColumnNames=('HEAD_VALUE_1','HEAD_VALUE_2','HEAD_VALUE_3','HEAD_VALUE_4','HEAD_VALUE_5','HEAD_VALUE_6','HEAD_VALUE_7','HEAD_VALUE_8','HEAD_VALUE_9')
reportrep1Name='Report_rep1_'
rep1ReportType='rep1'
rep2ColumnNames=('HEAD_VALUE_1','HEAD_VALUE_2','HEAD_VALUE_3','HEAD_VALUE_4','HEAD_VALUE_5','HEAD_VALUE_6','HEAD_VALUE_7')
reportrep2Name='Report_rep2_'
rep2ReportType='rep2'