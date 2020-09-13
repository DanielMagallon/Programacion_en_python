import sys
from Mysqsl_module import mysql

try:
    db_connection = mysql.connect("localhost", "root", "root", "SafeEntry")

    print("Connected")

    cursor = db_connection.cursor()

except:
    print("Can't connect to database")
    sys.exit(-1)

def closeAll():
    cursor.close()
    db_connection.close()


def exeProcedure(procedure_name, values: list, outParametersIndex=()) -> str:

    outs = ''

    for index in outParametersIndex:
        values.insert(0, "@var")
        outs += '@_' + procedure_name + "_" + str(index) + ","

    outs= outs[:len(outs)-1]

    cursor.callproc(procname=procedure_name, args=values)
    cursor.execute('SELECT ' + outs)
    db_connection.commit()
    result = cursor.fetchone()
    return result

def insertData(table, **kwargs):
    keys = ', '.join(list(kwargs.keys()))

    values = ""
    for val in kwargs.values():
        values += "'" + str(val) + "', "

    values = values[0:len(values) - 2]

    print(values)

    query = f"INSERT INTO {table} ({keys}) VALUES ({values})"
    print(query)

    cursor.execute(query)
    db_connection.commit()

    print(cursor.rowcount, "Record inserted successfully into Laptop table")
