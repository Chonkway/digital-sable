import discord
from discord import ui
import json
import logging
from discord import app_commands
import traceback


TEST_GUILD = discord.Object(GuildID)


class MyClient(discord.Client): #Client connection to discord
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        
        #app_tree instance required to use slash commads
        self.tree = app_commands.CommandTree(self)
    
    
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return     
        
    async def setup_hook(self) -> None: #Sync app command to API
        await self.tree.sync(guild=TEST_GUILD)   


class Submission(discord.ui.Modal, title='Feature Suggestions'): #Class for Submission command
    name = discord.ui.TextInput(label = 'Name', placeholder='Enter your name here...')
    suggestion = discord.ui.TextInput(label='Enter your suggestion', style = discord.TextStyle.long, placeholder='Enter your suggestion here...', required=True)
    
    async def on_submit(self, interaction: discord.Interaction):
        
        await interaction.response.send_message(f'Thank you for your submission {self.name}!', ephemeral = True)
        
        submission_dict = { f"{self.name}":f'{self.suggestion}'}
        with open('submissions.json', 'a+') as outfile:
            json.dump(submission_dict, outfile)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        error = traceback.print_tb(error.__traceback__) #Ensures we know what the error is
        await interaction.response.send_message(f'Oops! Something went wrong. Type: {error}', ephemeral = True)

client = MyClient()

@client.tree.command(description='Submit feature requests for adding to the bot')
async def submission(interaction: discord.Interaction):
    await interaction.response.send_modal(Submission()) #Sends modal submission through the Submission class 
    await interaction.response.defer()




























# logging.basicConfig(level=logging.INFO) #Logs info to console, commented out since it clogs stuff
logger = logging.getLogger('discord')   #Send logging debug info to a file 
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client.run('token')
