#import mysql.connector
#from mysql.connector import errorcode

#try:
#  cnx = mysql.connector.connect(user='scott',
#                                database='testt')
#except mysql.connector.Error as err:
#  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#    print("Something is wrong with your user name or password")
#  elif err.errno == errorcode.ER_BAD_DB_ERROR:
#    print("Database does not exist")
#  else:
#    print(err)
#else:
#  cnx.close()

#cursor = conn.cursor()

#cursor.execute("""
#            SELECT ID, FirstName, LastName, Street, City, ST, Zip
#            FROM Students
#            """)

#rows = cursor.fetchall()

## Convert query to row arrays

#rowarray_list = []
#for row in rows:
#    t = (row.ID, row.FirstName, row.LastName, row.Street,
#         row.City, row.ST, row.Zip)
#    rowarray_list.append(t)