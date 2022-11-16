import mysql.connector

class databaseManager():

    def __init__(self):
        pass

    def addToDb(self, activityName, category, deadline):
        pass

    def delInDb(self, val):
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()

        if (val != ''):
            sql = "DELETE FROM List_of_Activities WHERE ActivityID = %s"
            cursor.execute(sql, [val[0]])
        mydb.commit()
        mydb.close()

    def completeInDb(self, vals):
        pass

    def selectOngoingDb(self):
        pass

    def selectIdleDb(self):
        pass

    def selectCompletedByCategoryDb(self, category):
        pass