#!/usr/bin/python3.7
import discord
from command import Command
import shelve
from notebook import Notebook

client = discord.Client()

notebook = None
id = None

with shelve.open("storage.db") as db:
    if "notebook" not in db:
        print("Remaking notebook")
        db["notebook"] = Notebook()
    if "id" not in db:
        db["id"] = input("Give me a token: ")
    notebook = db["notebook"]
    id = db["id"]



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        output = "```\n"
        print(notebook.commandDict.items())
        for x, y in notebook.commandDict.items():
            output = output + '$' + x + ": " + y.description + "\n"
        output = output + "Only the those with the following ids can run these:\n"
        for x in notebook.userid:
            output = output + str(x) + "\n"

        await message.channel.send(output + "```")
    elif message.content.startswith('$'):
        if (message.author.id in notebook.userid):
            for x, y in notebook.commandDict.items():
                if message.content.startswith('$' + x):
                    out, err = y.run()
                    if (err != None):
                        await message.channel.send(err)
                    else:
                        await message.channel.send("No issues!")

                    break


client.run(id)

