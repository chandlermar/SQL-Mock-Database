Chandler Martin
CS333 Final Project
MOCK SQL DATABASE
Create and manage directories and files within a mock SQL Database using the chosen commands.

Approx Code Coverage: 

    Name          Stmts   Miss  Cover   Missing
    -------------------------------------------
    Database.py      56     30    46%   46-49, 57-91
    PA1.py           27      3    89%   57-60
    Parser.py         4      0   100%
    Table.py         41      1    98%   50
    test_db.py       36      0   100%
    -------------------------------------------
    TOTAL           164     34    79%

To Test:

    ***NOTE: Before testing, all created directories through the program must be deleted, including "db_test" which is created and persists after test execution to indicate successful testing.
             The tests are run before program execution, so the program can be executed like normal after testing commands are inputted if the user chooses.
             Another 

    coverage run PA1.py
    (Type 'EXIT' to exit the program loop or force quit with CNTRL+C)
    coverage report -m

To run: 

    Python3 PA1.py

        Commands:
            CREATE DATABASE db_1                                        (Creates new folder/directory)
            DROP DATABASE db_1                                          (Deletes folder/directory)
            USE db_1                                                    (Navigates into directory to allow table manipulation)
            CREATE TABLE tbl_1 (a1 int, a2 varchar(20));                (Creates new table/file within directory youre in)
            DROP TABLE tbl_1                                            (Deletes table/file)
            SELECT * FROM tbl_1                                         (Outputs content of chosen table)