from doctest import debug_script
from typing import Optional
import discord
from discord import app_commands
from discord.ui import View
import json
import traceback
from . import embeds
"""
Utility extension for SabBot
"""

class Submission(discord.ui.Modal, title='Feature Suggestions'):
    """
    Submission Modal for SabBot. When called, a popup will appear with the information filled in this class.
    """
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
        


class SableSearch(View):    #Inherit View to create UI
    """ Button Menu for SableSearch
    """
    #   I have no idea what this is but thank you Indian guy on youtube for solving this for me 
    def __init__(self, pages: list, timeout: float, user: Optional[discord.Member]=None) -> None:
        super().__init__(timeout=timeout)
        
        self.current_page = 0
        self.pages = pages
        self.user = user
        self.length = len(self.pages) - 1 #Ensure length count starts at 0
        
    async def update(self, page:int):
        self.current_page = page
        if page == page:
            self.children[page].disabled = True #Disable current button page? I think
        
    @discord.ui.button(style=discord.ButtonStyle.blurple)
    async def main_page(self, interaction , button):
        pass
    
    @discord.ui.button(style=discord.ButtonStyle.gray)
    async def open_source(self, interaction , button):
        pass
    
    @discord.ui.button(style=discord.ButtonStyle.green)
    async def lgbt(self, interaction , button):
        pass
    
    @discord.ui.button(style=discord.ButtonStyle.red)
    async def exit(self, interaction , button):
        pass
        
    # @app_commands.command(description = 'SableSearch test') #Parent command?
    # async def sablesearch(interaction: discord.Interaction):
    #     interaction.response.send_message(embed=embeds.main_embed)
    
    # @app_commands.command(description='List of opensource projects')    
    # async def opensource(interaction: discord.Interaction):    #Default Navigation Menu
    #     interaction.response.send_message(embed=embeds.OS_embed)
    
    
    # @app_commands.command()
    # async def lgbt(interaction: discord.Interaction):
    #     pass

        
    