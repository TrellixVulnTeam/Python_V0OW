import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=IRIS-CSG-1634;DATABASE=JohnDoeBox;')

cursor = cnxn.cursor()

cursor.execute('SELECT * FROM JohnDoeBox.dbo.USERS;')

for user in cursor:
    print(user)