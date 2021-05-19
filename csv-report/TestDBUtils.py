from utils import DBUtils, DBQuerys

print("Init of Test DB Utils")

env='Test'

print(DBQuerys.queryReportrep2.format('InitDateTest','EndDateTest'))
print(DBQuerys.queryReportrep1.format('InitDateTest','EndDateTest'))
print(DBQuerys.queryTest)

#Test uso utilitarios
connection = DBUtils.getDbConnection(env)
cursor = connection.cursor()
cursor.execute(DBQuerys.queryTest)
for rows in cursor:
    print('Result => {}'.format(rows[0]))

connection.close()


print("End of Test DB Utils")
