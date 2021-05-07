
from utils import AppUtils, AppParams


print("Init of Unify Report")

env='Test'
print('Unified Reports, Environment {}'.format(env))


AppUtils.unifiedReports(AppParams.basePath, AppParams.reportrep1Name ,AppParams.rep1ReportType, env, AppParams.rep1ColumnNames)

AppUtils.unifiedReports(AppParams.basePath, AppParams.reportrep2Name, AppParams.rep2ReportType, env, AppParams.rep2ColumnNames)

print("End of Unify Report")
