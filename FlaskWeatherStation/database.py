import sqlite3


class database:

    __dbconn = None
    __dbconnection = None

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if database.__dbconn == None:
            database()
            return database.__dbconn
    
    def __init__(self):        
        if database.__dbconn != None:
            raise Exception("This class is a database!")
        else:
            database.__dbconn = self
            self.__dbconnection = sqlite3.connect('users.db')



    def createtable(self):        
        #self.__dbconnection.cursor().execute("""INSERT INTO users VALUES ('Steven', 'Duffy', 'SDuffy', 'Dragon')""")
        #self.__dbconnection.commit()
        #command = self.__dbconnection.cursor()
        #command.execute("SELECT * FROM users;")
        #print(command.fetchall())
        #self.__dbconnection.commit()
        #self.__dbconnection.close()
#.execute("""create table users (firstname) """)
database.getInstance().createtable()


# dbconn = sqlite3.connect('users.db')

# cursor = dbconn.cursor()

# cursor

# dbconn.commit()

# dbconn.close()
