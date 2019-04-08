import sqlite3


class database:

    def __init__(self):
        self.db = sqlite3.connect('users.db')
        self.pointer = self.db.cursor()
    
    def verify_user(self, credentials):        
        query = self.pointer.execute("SELECT password FROM users WHERE user_name = :username", credentials)
        stored_password = query.fetchone()        
        self.db.commit()
        self.db.close()
        print(stored_password)
        if (stored_password == None):
            return False
        if (credentials["password"] == stored_password[0]):
            return True
        else:
            return False
        

#credentials = {}
#credentials["username"] = "SDuffy"
#credentials["password"] = "Dragon"
#d = database()
#print(d.verify_user(credentials))

			

#class database_two:
#
#   __dbconn = None
#    __dbconnection = None
#
#    @staticmethod
#    def getInstance():
#        """ Static access method. """
#        if database.__dbconn == None:
#            database()
#            return database.__dbconn
#
#    def __init__(self):
#        if database.__dbconn != None:
#            raise Exception("This class is a database!")
#        else:
#            database.__dbconn = self
#            self.__dbconnection = sqlite3.connect('users.db')
#
#    def create_table(self):
#        x = self.__dbconnection.cursor()
#        x.execute("""Select first_name from users where second_name = 'Gaitan'""")
#        print(x.fetchone())
#
#       self.__dbconnection.commit()
#        #command = self.__dbconnection.cursor()
#        #command.execute("SELECT * FROM users;")
#        #print(command.fetchall())
#        #self.__dbconnection.commit()
#        self.__dbconnection.close()
#.execute("""create table users (firstname) """)
#       database.getInstance().create_table()
#
#
# dbconn = sqlite3.connect('users.db')

# cursor = dbconn.cursor()

# cursor

# dbconn.commit()

# dbconn.close()
