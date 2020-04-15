import shelve
from command import Command
from notebook import Notebook

potebook = None
with shelve.open("storage.db") as db:
    potebook = db["notebook"]
    key = input("Could I have the discord command?")

command = input("Please enter the command to be run: ")
description = input("Please give me a description: ")
potebook.commandDict[key] = Command(command, description)
print(potebook.commandDict[key].cmd)
print(potebook.commandDict.items())

with shelve.open("storage.db") as db:
    db["notebook"] = potebook
    print(db["notebook"].commandDict.items())

print("All done!")
