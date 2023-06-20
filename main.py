import discord
from discord import app_commands
from discord.ext import commands
import random
import datetime
import calendar
import time
import asyncio
import random
import datetime
import os
ts = calendar.timegm(time.gmtime())

from discord.ext import commands 

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=".", intents=intents)

intents.message_content = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

liste_embed =["Kin'Sa"]



@bot.event
async def on_ready():
    print(f"{bot.user.name} est OP")

    try:
        synced = await bot.tree.sync(guild=discord.Object(id=1120457058932768869))
        print(f"Synced {len(synced)} commands")

    except Exception as e:
        print(e)

def is_owner():
    def predicate(Interaction: discord.Interaction):
        if Interaction.user.id == Interaction.guild.owner.id:
            return True
    return app_commands.check(predicate)




############################################################################################################################################################################



###TEST###

@bot.tree.command(guild=discord.Object(id=1120457058932768869), name="test", description="Commande de Test")
async def test_slash(Interaction: discord.Interaction):
    await Interaction.response.send_message("Ceci est un test")

@bot.tree.command(guild=discord.Object(id=1120457058932768869), name="owner", description="Commande pour l'owner")
@is_owner()
async def owner_slash(Interaction : discord.Interaction):
    await Interaction.response.send_message(f"Hello !", ephemeral=True)


###############################################################################################################################################################################

###MODERATION###

#BAN
@bot.tree.command(guild=discord.Object(id=1120457058932768869), name="ban", description="Commande de Ban")
@is_owner()
@app_commands.describe(
    user="Le membre à bannir",
    reason="Raison du bannissement",
)
async def ban_slash(interaction: discord.Interaction, user: discord.Member, reason: str = None):
     if reason is None:
         reason = "Aucune raison fournie"

     channel = interaction.guild.get_channel(1120476649415262318)

     await interaction.guild.ban(user, reason=reason)

     embed = discord.Embed(title="Bannissement", description="Un Modérateur a banni un membre !", color=0xff0000)
     embed.add_field(name="Informations :", value=f"Utilisateur : {user.mention}\nDate : <t:{ts}:R>\n Modérateur : {interaction.user.mention}\nRaison :\n{reason}", inline=False)
     embed.set_footer(text=random.choice(liste_embed))
     embed.timestamp = datetime.datetime.now()

     await interaction.response.send_message(embed=embed, ephemeral=False)
     await channel.send(embed=embed)

@ban_slash.error
async def say_error(Interaction: discord.Interaction, error):
    await Interaction.response.send_message("Tun'as pas la permission d'utiliser cette permission")


#CLEAR
@bot.tree.command(guild=discord.Object(id=1120457058932768869), name="clear", description="Commande de Clear")
@is_owner()
@app_commands.describe(
    amounts="Message à clear",
    channel="Channel ou le msg est del"
)
async def clear_slash(interaction: discord.Interaction, amounts: int, channel: discord.TextChannel = None):
     
     if channel is None:
         channel = interaction.channel

     channel1 = interaction.guild.get_channel(1120476649415262318)

     embed= discord.Embed(title="Message Supprimés", description="Un modérateur à clear les messages", color=discord.Color.green())
     embed.add_field(name="Infos Modérateur :", value=f"Utilisateur : {interaction.user.mention}\n Nom : {interaction.user.name}#{interaction.user.discriminator}", inline=False)
     embed.add_field(name="Infos Message :", value=f"Date : <t:{ts}:R>\n Salon : {channel.mention}\n Nombre : {amounts}", inline=False)
     embed.set_footer(text=random.choice(liste_embed))
     embed.timestamp=datetime.datetime.now()

     await interaction.response.send_message(embed=embed, ephemeral=False)
     await channel1.send(embed=embed)
     await channel.purge(limit=amounts)

@clear_slash.error
async def say_error(Interaction: discord.Interaction, error):
    await Interaction.response.send_message("Tun'as pas la permission d'utiliser cette permission")

bot.run(PREMIER DEGRES J'L'AVAIS LEAK COMME UN BOUFFON)
