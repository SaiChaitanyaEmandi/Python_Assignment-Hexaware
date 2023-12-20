import mysql.connector as sql
from mysql.connector import Error
from Assignment.UTIL.PROPERTYUTIL import PropertyUtil


class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            try:
                connection_string = PropertyUtil.getPropertyString()
                DBConnection.connection = sql.connect(**connection_string)

                if DBConnection.connection.is_connected():
                    print("Connected to the database")
            except Error as e:
                print(f"Error: {e}")

        return DBConnection.connection