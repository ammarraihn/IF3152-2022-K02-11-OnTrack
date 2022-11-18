import mysql.connector

class databaseManager():

    def __init__(self):
        pass

    def addToDb(self, activityName, category, deadline):
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO list_of_activities (ActivityName, CategoryName, Deadline, isDone) VALUES ('{}', '{}', '{}', FALSE)".format(
            activityName, 
            category, 
            deadline
        ))
        mydb.commit()
        mydb.close()

    def delInDb(self, vals):
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()

        # Bisa ngedelete dari salah satu ongoing atau idle tree, atau bisa complete dari keduanya langsung
        for val in vals:
            if (val != ''):
                sql = "DELETE FROM list_of_activities WHERE ActivityID = %s"
                cursor.execute(sql, [val[0]])
        mydb.commit()
        mydb.close()

    def completeInDb(self, vals):
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()

        # Bisa ngecomplete dari salah satu ongoing atau idle tree, atau bisa complete dari keduanya langsung
        for val in vals:
            if (val != ''):
                sql = "UPDATE list_of_activities SET isDone = TRUE WHERE ActivityID = %s"
                cursor.execute(sql, [val[0]])
        mydb.commit()
        mydb.close()

    def selectOngoingDb(self):
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("SELECT ActivityID, ActivityName, CategoryName, Deadline FROM list_of_activities WHERE Deadline = CURDATE() AND isDone = FALSE")
        result = cursor.fetchall()
        mydb.commit()
        mydb.close()
        return(result)

    def selectIdleDb(self):
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("SELECT ActivityID, ActivityName, CategoryName, Deadline FROM list_of_activities WHERE Deadline > CURDATE() AND isDone = FALSE ORDER BY Deadline ASC")
        result = cursor.fetchall()
        mydb.commit()
        mydb.close()
        return(result)

    def selectCompletedByCategoryDb(self, category):
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("SELECT ActivityName, Deadline FROM list_of_activities WHERE CategoryName = %s AND isDone = TRUE ORDER BY Deadline ASC", [category])
        result = cursor.fetchall()
        mydb.commit()
        mydb.close()
        return(result)

        

