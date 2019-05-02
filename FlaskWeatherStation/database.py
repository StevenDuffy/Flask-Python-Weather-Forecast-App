import sqlite3

# Provides a connection to the database.
class database:

    # Creates database connection and cursor.
    def __init__(self):
        self.db = sqlite3.connect('users.db')
        self.pointer = self.db.cursor()
    
    # Checks if given user credentials match a set credentials stored in the databse.
    def verify_user(self, credentials):        
        query = self.pointer.execute("SELECT password FROM users WHERE username = :username", credentials)
        stored_password = query.fetchone()        
        self.db.commit()        
        # print(stored_password)
        if (stored_password == None):
            return False
        if (credentials["password"] == stored_password[0]):
            return True
        else:
            return False

    # Checks if given credentials already exist in the database.
    def check_username_exists(self, credentials): 
        query = self.pointer.execute("SELECT username FROM users WHERE username = :username", credentials)
        username_found = query.fetchone()        
        self.db.commit()        
        # print(stored_password)
        if (username_found == None):
            return False
        else:
            return True

    # Adds given credentials to the database.
    def add_user(self, credentials):   
        self.db    
        self.pointer.execute("INSERT INTO users VALUES (:username, :first_name, :second_name, :password)", credentials)               
        self.db.commit()
        
    # Closes connection to the database.
    def close(self):
        self.db.close()
             
        
   
        

#credentials = {}
#credentials["username"] = "SDuffy"
#credentials["password"] = "Dragon"
#credentials["first_name"] = "David"
#credentials["second_name"] = "Duffy"


### Database queries 
#
#d = database()
#print(d.add_user(credentials))
#c = d.pointer

#
### Database creation ###
#
# c.execute("""CREATE TABLE users (username TEXT PRIMARY KEY NOT NULL,
#                                first_name TEXT NOT NULL,
#                                second_name TEXT NOT NULL,
#                                password TEXT NOT NULL);""")

#d.db.commit()
#d.db.close()
# print(d.verify_user(credentials))

			

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
