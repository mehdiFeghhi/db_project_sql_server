import pyodbc


connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=DESKTOP-KQCRNC1;'
                            'DATABASE=projectDB;'
                            'Trusted_Connection=yes;')

# cursor = connection.cursor()
# cursor.execute('select * from CUSTOMER')
# print(cursor.rowcount)
# for item in cursor:
#     print(item)
#     print(type(item))