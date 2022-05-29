# from ast import Interactive
# from code import interact
# from dis import disco
# from email import message
# from inspect import formatannotation
# from operator import imod
# from tokenize import group
import discord
from discord import ui
import json
import logging
from discord import app_commands
import traceback
from pathlib import Path
import random, os
from ext import utility

TEST_GUILD = discord.Object(id=)
cwd = Path(__file__).parent


class MyClient(discord.Client): #Client connection to discord
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        intents.message_content = True
        
        #app_tree instance required to use slash commads
        self.tree = app_commands.CommandTree(self)
    

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
             
        if 'sunshine' in message.content.lower():   #//Fix absolute path to be relative
            await message.reply(file=discord.File(fp='/home/sable/Pictures/fear_me_again.png'))
            
        if 'worldgaming' in message.content.lower():   #//Fix absolute path to be relative
            await message.reply(file=discord.File(fp='/home/sable/Pictures/image0.jpg'))
            
        if 'download house' in message.content.lower():   #//Fix absolute path to be relative
            await message.reply(file=discord.File(fp='/home/sable/Pictures/house.jpg'))
            
        
    async def setup_hook(self) -> None: #Sync app command to API
        print(f'Synced to designated guild')
        await self.tree.sync(guild=discord.Object(id=))
             




client = MyClient()

@client.tree.command(description='Submit feature requests for adding to the bot')
async def submission(interaction: discord.Interaction):
    await interaction.response.send_modal(utility.Submission()) #Sends modal submission through the Submission class 
    await interaction.response.defer()
    

@client.tree.command(description='Receive a Luigi :)', guilds=[])
async def luigi(interaction: discord.Interaction):
    resc = str(cwd) + '/resources/luigi/'
    r = random.choice(os.listdir(resc)) 
    file = discord.File(resc+r)
    print(f'Sent {file.filename}')
    await interaction.response.send_message(file=file)


#Sable Search will be meant to be categorized into a command group class eventually
# client.tree.add_command(utility.SableSearch(), guild=TEST_GUILD)


#-------------------------------------------------------------



# logging.basicConfig(level=logging.INFO) #Logs to console
logger = logging.getLogger('discord')   #Send logging debug info to a file 
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client.run('')
