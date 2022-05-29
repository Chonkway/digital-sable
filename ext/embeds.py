import discord

"""
Hosts embed information
"""
#Main/Navigation embed
main_embed=discord.Embed(title="Sable Search", description="Welcome to SableSearch! Here you can find community-submitted resources categorized into groups.\nYou can use `/sablesearch []` where `[]` is the subcommand relating to the group you want to access or just use the buttons on this page to navigate.", 
                            color=0xf8e45c,
                            
                            )
main_embed.set_author(name='SabBot', url='https://github.com/Chonkway')
main_embed.set_footer(text='SableSearch Navigation')

#----
# Open Source Sites embed
OS_embed=discord.Embed(title="Sable Search", description= 'A list of all submitted open-source projects in Sable Search.',
                            color=0xf8e45c,
                            
                            )
OS_embed.set_author(name='SabBot', url='https://github.com/Chonkway')
OS_embed.set_footer(text='SableSearch Open-Sourced')
OS_embed.add_field(name='Bionic Reading', value='https://bionic-reading.com/', inline=False)


#