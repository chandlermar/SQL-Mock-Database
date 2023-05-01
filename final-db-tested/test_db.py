from Database import Database
from Table import Table
from Parser import Parser
import unittest

class testCases(unittest.TestCase):
  database = Database()
  table = Table()
  parser = Parser()

  #Tests that databases are created when valid, arent created when already existing.
  def test_db_create(self, startingDir):
    assert(self.database.create_database("db_1", startingDir) == True)
    assert(self.database.create_database("db_test", startingDir) == True)
    assert(self.database.create_database("db_test", startingDir) == False)
    assert(self.database.create_database("db_3", startingDir) == True)

  #Tests that databases are dropped when valid
  def test_db_drop(self, startingDir):
    assert(self.database.drop_database("db_1", startingDir) == True)
    assert(self.database.drop_database("db_4", startingDir) == False)

  #Tests that input is parsed correctly
  def test_parser(self):
    assert(self.database.parser.input_parser("CREATE DATABASE db_1;") == ["CREATE", "DATABASE", "db_1;"])

  #Tests that when a database is selected that isTable flag is flipped, database to be used is correct, and action is completed.
  def test_use_db(self, startingDir): #NOT IN MAIN
    assert(self.database.isTable == 0)
    assert(self.database.use_database(["USE", "db_test"], startingDir) == True)
    assert(self.table.currentDatabase == "db_test")
    assert(self.database.isTable == 1)

  #Tests to that when valid a table can be created, and when existing name is taken table isnt created.
  def test_table_create(self, startingDir):
    assert(self.table.create_table(startingDir, ["CREATE", "TABLE", "tbl_1", "(a1 int, a2 varchar(20));"]) == True)
    assert(self.table.create_table(startingDir, ["CREATE", "TABLE", "tbl_2", "(a2 int, a3 varchar(22));"]) == True)
    assert(self.table.create_table(startingDir, ["CREATE", "TABLE", "tbl_2", "(a2 int, a3 varchar(22));"]) == False)

  #Tests that table is dropped
  def test_table_drop(self, startingDir):
    assert(self.table.drop_table(startingDir, ["DROP", "TABLE", "tbl_1"]) == True)
    assert(self.table.drop_table(startingDir, ["DROP", "TABLE", "tbl_4"]) == False)
    

  #Tests that table select function prints table contents
  def test_table_select(self, startingDir):
    assert(self.table.select_data(startingDir, ["SELECT", "*", "FROM", "tbl_2"]) == True)
    assert(self.table.select_data(startingDir, ["SELECT", "*", "FROM", "tbl_4"]) == False)

  #Tests that when generating two cards that equal a blackjack, that the checkPlayerBJ function returns True
  def test_cleanup(self, startingDir):
    self.database.isTable = 0
    assert(self.database.drop_database("db_3", startingDir) == True)

  