#Chandler Martin
#10/10/22
#CS457_PA1

#from ast import parse
import os
import sys
from Database import Database
from Table import Table
from Parser import Parser
from test_db import testCases

startingDir = os.getcwd()


#Runs tests then launches main program
#Loops until user enters EXIT.
#When a valid command is detected, enter check_command function.
#InputParser is called to seperate user input and passed into check_command
def main():

    database = Database()
    table = Table()
    parser = Parser()
    test = testCases()
    
    #Creating and destroying database
    test.test_db_create(startingDir)

    test.test_db_drop(startingDir)

    # Test parser
    test.test_parser()

    #Test use func
    test.test_use_db(startingDir)

    #Test table creation
    test.test_table_create(startingDir)

    #Test table deletion
    test.test_table_drop(startingDir)

    #Test table print
    test.test_table_select(startingDir)

    #Remove remaining test databases
    test.test_cleanup(startingDir)

    #Clear screen, start program
    os.system('cls')

    #Main program
    while True:
    
        userInput = input()
        if (userInput == 'EXIT'):
            break
        else:
            database.check_command(parser.input_parser(userInput), startingDir, table)

        

if __name__ == "__main__":
    main()
