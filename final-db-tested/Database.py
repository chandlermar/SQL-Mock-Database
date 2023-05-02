import os
from Parser import Parser
from Table import Table

class Database:

    isTable = 0
    
    parser = Parser()

    def create_database(self, dbName, startingDir):
        dir = os.path.join(startingDir, dbName)
        if not os.path.exists(dir):
            os.mkdir(dir)
            print("Database " + dbName + " created.") # pragma: no cover
            return True
        else:
            print("!Failed to create database " + dbName + " because it already exists.") # pragma: no cover
            return False

    def drop_database(self, dbName, startingDir):
        dir = os.path.join(startingDir, dbName)
        if os.path.exists(dir):
            
            os.rmdir(dir)
            print("Database " + dbName + " deleted.") # pragma: no cover
            return True
        else:
            print("!Failed to delete " + dbName + " because it does not exist.") # pragma: no cover
            return False
        
    def use_database(self, parseTokens, startingDir):
         dir = os.path.join(startingDir, parseTokens[1])
         if os.path.exists(dir):
             os.chdir(dir)
        
             print ("Using database " + parseTokens[1] + ".") # pragma: no cover

             Table.currentDatabase = parseTokens[1]
             self.isTable = 1
             return True
                    
         else:
             Table.currentDatabase = ""
             self.isTable = 0
             print("Database does not exist.") # pragma: no cover
             return False

    #Checks what command type was entered (CREATE, DROP, SELECT, etc). 
    #If a dual meaning command is entered (such as CREATE for either a table or database) the isTable variable is checked to see which routine loop the program is currently in.
    #isTable=0 -> Not currently in a directory
    #isTable=1 -> Currently in a directory
    def check_command(self, parseTokens, startingDir, table):

        if (self.isTable == 0):
            if (parseTokens[0] == "CREATE"):
                if (parseTokens[1] == "DATABASE"):
                    self.create_database(parseTokens[2], startingDir)
                else:
                    print("Invalid Command")
            elif (parseTokens[0] == "DROP"):
                if (parseTokens[1] == "DATABASE"):
                    self.drop_database(parseTokens[2], startingDir)
                else:
                    print("Invalid Command")
            elif (parseTokens[0] == "USE"):
                self.use_database(parseTokens, startingDir)
            else:
                print("Invalid Command")


        elif (self.isTable == 1):
            if (parseTokens[0] == "CREATE"):
                if (parseTokens[1] == "TABLE"):
                    table.create_table(startingDir, parseTokens)
                else:
                    print("Invalid Command")
            elif (parseTokens[0] == "DROP"):
                if (parseTokens[1] == "TABLE"):
                    table.drop_table(startingDir, parseTokens)
                else:
                    print("Invalid Command")
            elif (parseTokens[0] == "SELECT"):
                if (parseTokens[1] == '*'):
                    table.select_data(startingDir, parseTokens)
            elif (parseTokens[0] == "USE"):
                    self.use_database(parseTokens, startingDir)
            else:
                print ("Invalid Command")