from Database import Database
from Table import Table
from Parser import Parser
import os
import unittest

class testCases(unittest.TestCase):
  database = Database()
  table = Table()
  

  startingDir = os.getcwd()

  #Tests that databases are created when valid, arent created when already existing.
  def test_db_create(self):
    assert(self.database.create_database("db_1", self.startingDir) == True)
    assert(self.database.create_database("db_testy", self.startingDir) == True)
    assert(self.database.create_database("db_testy", self.startingDir) == False)

  #Integration test
  def int_1(self):
    assert(self.database.parser.input_parser("CREATE DATABASE db_2") == ["CREATE", "DATABASE", "db_2"])
    parseTokens = self.database.parser.input_parser("CREATE DATABASE db_2")
    assert(self.database.check_command(parseTokens) == True)
  
  #Integration test
  def int_2(self):
    assert(self.database.parser.input_parser("DROP DATABASE db_2") == ["DROP", "DATABASE", "db_2"])
    parseTokens = self.database.parser.input_parser("DROP DATABASE db_2")
    assert(self.database.check_command(parseTokens) == True)
    

  #Tests that databases are dropped when valid
  def test_db_drop(self):
    assert(self.database.drop_database("db_1", self.startingDir) == True)
    assert(self.database.drop_database("db_4", self.startingDir) == False)

  #Tests that input is parsed correctly
  def test_parser(self):
    assert(self.database.parser.input_parser("CREATE DATABASE db_1") == ["CREATE", "DATABASE", "db_1"])

  #Tests that when a database is selected that isTable flag is flipped, database to be used is correct, and action is completed.
  def test_use_db(self): 
    assert(self.database.isTable == 0)
    assert(self.database.use_database(["USE", "db_testy"], self.startingDir) == True)
    assert(self.table.currentDatabase == "db_testy")
    assert(self.database.isTable == 1)

  #Integration Test
  def int_3(self):
    assert(self.database.parser.input_parser("CREATE TABLE tbl_5") == ["CREATE", "TABLE", "tbl_5"])
    assert(self.table.create_table(self.startingDir, ["CREATE", "TABLE", "tbl_5", "(a7 int, a1 uint(64));"]) == True)

  #Tests to that when valid a table can be created, and when existing name is taken table isnt created.
  def test_table_create(self):
    assert(self.table.create_table(self.startingDir, ["CREATE", "TABLE", "tbl_1", "(a1 int, a2 varchar(20));"]) == True)
    assert(self.table.create_table(self.startingDir, ["CREATE", "TABLE", "tbl_2", "(a2 int, a3 varchar(22));"]) == True)
  
  #Tests that table select function prints table contents
  def test_table_select(self):
    assert(self.table.select_data(self.startingDir, ["SELECT", "*", "FROM", "tbl_4"]) == False)

  # Tests that table is dropped
  def test_table_drop(self):
    assert(self.table.drop_table(self.startingDir, ["DROP", "TABLE", "tbl_1"]) == True)
    assert(self.table.drop_table(self.startingDir, ["DROP", "TABLE", "tbl_2"]) == True)
    assert(self.table.drop_table(self.startingDir, ["DROP", "TABLE", "tbl_4"]) == False)
    

  


  