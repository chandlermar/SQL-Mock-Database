#Chandler Martin
#4/30/23
#CS333_Final

import os
from Database import Database
from Table import Table
from Parser import Parser
from test_db import testCases

startingDir = os.getcwd()


#Launches main program
#Loops until user enters EXIT.
#When a valid command is detected, enter check_command function.
#InputParser is called to seperate user input and passed into check_command
def main():

    database = Database()
    table = Table()
    parser = Parser()
    test = testCases()

    #Main program
    while True:
    
        userInput = input()
        if (userInput == 'EXIT'):
            break
        else:
            database.check_command(parser.input_parser(userInput), startingDir, table)

        

if __name__ == "__main__":
    main()
