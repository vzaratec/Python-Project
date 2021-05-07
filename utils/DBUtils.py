from utils import AppParams
import cx_Oracle

# Connection to database
# if needed, place an 'r' before any parameter in order to address special characters such as '\'. 
# For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

def getDbConnection(environment):
    print('Open Connection. Environment {}'.format(environment))
    return cx_Oracle.connect(user=AppParams.dbUser, password=AppParams.dbPass, dsn=getDbTns(environment))

def getDbTns(environment):
    if environment == 'Amb1':
        return cx_Oracle.makedsn(AppParams.dbHostAmb1, AppParams.dbPortAmb1, service_name=AppParams.dbSvcNameAmb1)
    elif environment == 'Amb2':
        return cx_Oracle.makedsn(AppParams.dbHostAmb2, AppParams.dbPortAmb2, service_name=AppParams.dbSvcNameAmb2)
    return object()
