
class DBQuerys :

        def getQuery(self) :
                self.queryTest = queryTest
                self.queryReportrep1 = queryReportrep1
                self.queryReportrep2 = queryReportrep2


queryReportrep1=""" SELECT sysdate+60 from dual """

queryReportrep2=""" SELECT sysdate-60 from dual """

queryTest = """ SELECT sysdate from dual """