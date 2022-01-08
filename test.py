import src.simpleUID as simpleUID

# print(simpleUID.database(cursor={
#     'cursor': 'iets',
#     'table': 'FA_projectbase',
#     'column': 'project_id'
# }))

import mysql.connector

mydb = mysql.connector.connect(
  host="136.144.253.57",
  user="fa-fmm-test",
  password="FacoFaFMM.test-db21.allow",
  database="FMM_TEST"
)

cursor = mydb.cursor()


print(simpleUID.database(cursor={
    'cursor': cursor,
    'table': 'FA_projectbase',
    'column': 'project_id'
}, method="integer", prefix=12, length=100))