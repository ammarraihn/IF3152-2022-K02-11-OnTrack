import mysql.connector

class databaseManager():

    def __init__(self):
        pass

    def addToDb(self, activityName, category, deadline):
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO list_of_activities (ActivityName, CategoryName, Deadline, isDone) VALUES ('{}', '{}', '{}', FALSE)".format(
            activityName, 
            category, 
            deadline
        ))
        mydb.commit()
        mydb.close()

    def delInDb(self, vals):
        pass

    def completeInDb(self, vals):
        pass

    def selectOngoingDb(self):
        pass

    def selectIdleDb(self):
        pass

    def selectCompletedByCategoryDb(self, category):
        pass