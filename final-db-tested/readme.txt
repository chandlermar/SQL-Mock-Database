Chandler Martin
CS333 Final Project
MOCK SQL DATABASE
Create and manage directories and files within a mock SQL Database using the chosen commands.
*** Expected output if you wish to test with the commands provided in PA1_test.sql is in output.png ***

Approx Code Coverage: 

    Name          Stmts   Miss  Cover
    ---------------------------------
    Database.py      56     30    46%
    Parser.py         4      0   100%
    Table.py         41      5    88%
    test_db.py       43      8    81%
    ---------------------------------
    TOTAL           144     43    70%

To Test:

    ***NOTE: Before testing, all created directories through the program must be deleted, including "db_test" which is created and persists after test execution to indicate successful testing.
             The tests are run before program execution, so the program can be executed like normal after testing commands are inputted if the user chooses.

    docker build -t pa-final .
    docker run -it pa-final
    (Type 'EXIT' to exit the program loop or force quit with CNTRL+C)

To run: 

    Python3 PA1.py

        Commands:
            CREATE DATABASE db_1                                        (Creates new folder/directory)
            DROP DATABASE db_1                                          (Deletes folder/directory)
            USE db_1                                                    (Navigates into directory to allow table manipulation)
            CREATE TABLE tbl_1 (a1 int, a2 varchar(20));                (Creates new table/file within directory youre in)
            DROP TABLE tbl_1                                            (Deletes table/file)
            SELECT * FROM tbl_1                                         (Outputs content of chosen table)

                                                                        (**Note: Directories should be created and deleted first when running the program. You can not create/delete directories once youre
                                                                                 using a directory with the USE command. Additionally, tables can only be created/deleted once you are within a directory.)