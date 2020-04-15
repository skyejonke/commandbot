#!/usr/bin/python3.7
import discord
from command import Command
import shelve
from notebook import Notebook

client = discord.Client()

notebook = None

with shelve.open("storage.db") as db:
    if "notebook" not in db:
        db["notebook"] = Notebook()
    notebook = db["notebook"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        output = "```\n"
        for x, y in notebook.commandDict.items():
            output = output + '$' + x + ": " + y.description + "\n"
        output = output + "Only the those with the following ids can run these:\n"
        for x in notebook.userid:
            output = output + str(x) + "\n"

        await message.channel.send(output + "```")
    elif message.content.startswith('$'):
            for x, y in notebook.commandDict.items():
                if message.content.startswith('$' + x):
                    out, err = y.run()
                    if (err != None):
                        await message.channel.send(err)
                    else:
                        await message.channel.send("No issues!")

                    break


client.run('NzAwMTIwMzU2MzQ5ODA0NjM1.XpeUEg.6wuc_Ow1U-DLLOhsGRw_xEsOE10')

