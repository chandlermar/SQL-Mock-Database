import os

class Table:

    currentDatabase = ""

    def create_table(self, startingDir, parseTokens):
        dir = os.path.join(startingDir, self.currentDatabase)
        os.chdir(dir)
        if not os.path.exists(os.path.join(dir, parseTokens[2])):
            with open (parseTokens[2], 'w') as f:
                f.write(self.input_formatter(parseTokens))     
            print("Table " + parseTokens[2] + " created.") # pragma: no cover
            return True
        else:
            print("!Failed to create table " + parseTokens[2] + " because it already exists.") # pragma: no cover
            return False
        
    def drop_table(self, startingDir, parseTokens):
        dir = os.path.join(startingDir, self.currentDatabase)
        os.chdir(dir)
        if os.path.exists(os.path.join(dir, parseTokens[2])):
            os.remove(parseTokens[2])
            print("Table " + parseTokens[2] + " deleted.") # pragma: no cover
            return True
        else:
            print("!Failed to delete " + parseTokens[2] + " because it does not exist.") # pragma: no cover
            return False
        
    def select_data(self, startingDir, parseTokens):
        dir = os.path.join(startingDir, self.currentDatabase)
        os.chdir(dir)
        if os.path.exists(os.path.join(dir, parseTokens[3])):
            with open(parseTokens[3]) as f:
                print(f.readlines())
            return True
        else:
            print("!Failed to query table " + parseTokens[3] + " because it does not exist.") # pragma: no cover
            return False

    def input_formatter(self, parseTokens):
        tempString = ""
        parselen = len(parseTokens) - 1
        count = 3
        for x in parseTokens: #For all items starting from the index of table data entered, concatenate strings and add a space between each concatenated item in list.
            if (count <= parselen):
                if (count == 3):
                    tempString = tempString + parseTokens[count]
                else:
                    tempString = tempString + " " + parseTokens[count]
                count += 1

        finalString = tempString.replace(',',' |') #Remove the ',' character and replace with ' |' to achieve desired format.
        finalString = finalString[:len(finalString) - 1]
        finalString = finalString[:len(finalString) - 1] 
        finalString = finalString[1:]
        return (finalString)