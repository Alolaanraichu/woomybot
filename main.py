import discord
import random
import asyncio
import json
from discord.ext import commands
from songs import song
from weapons import weapon
description = '''sploon'''
BOT_PREFIX = ('!')
TOKEN = "NDYzODE3MDc5MDI4NzExNDM0.Dh7EpA.12HFkharb9uAbpmYl-abJWpeou4"
bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
#@bot.command
#if message.content.startswith('!hello'):
        #msg = ''.format(message)
        #await client.send_message(message.channel, msg)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

async def joined(ctx, member: discord.Member):
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def commands(ctx):
    await ctx.send('roll NdN, add N=N, play, songlist, weapons, woomy, agent8')

@bot.command()
async def songlist(ctx):
    await ctx.send('songs: i am octavio, splattack, splattack dedf1sh remix, calamari inkatation, inkopolis square, inkopolis plaza, nasty majesty, fly octo fly and happy little workers.')


@bot.command()
async def play(ctx):
    songs=[
        song("i_am_octavio", "https://www.youtube.com/watch?v=fYOi3xiC5cY"),
        song("splattack", "https://www.youtube.com/watch?v=wRytjitcSbw"),
        song("calamari_inkatation", "https://www.youtube.com/watch?v=rUGJN5tgQPE"),
        song("inkopolis_square", "https://www.youtube.com/watch?v=s_0IYJ7Fqk8"),
        song("inkopolis_plaza", "https://www.youtube.com/watch?v=NCq6D6cdcA4"),
        song("nasty_majesty", "https://youtu.be/0wXW-E9u2Cs"),
        song("fly_octo_fly", "https://youtu.be/Q2KAcA-ZADE" ),
        song("happy_little_workers","https://www.youtube.com/watch?v=-md51zrR5eg"),
        song("splattack_octo", "https://www.youtube.com/watch?v=NU25fgf4dyc")
    ]
    random.shuffle(songs)

    songUrl = songs.pop()
    await ctx.send(songUrl.url)
@bot.command()
async def weapons(ctx):
    weapons=[
    weapon("splatterjr", "https://cdn.wikimg.net/en/splatoonwiki/images/5/5e/S2_Weapon_Main_Splattershot_Jr..png"),
    weapon("aero", "https://cdn.wikimg.net/en/splatoonwiki/images/a/a1/S2_Weapon_Main_Aerospray_MG.png"),
    weapon("splatter", "https://cdn.wikimg.net/en/splatoonwiki/images/6/60/S2_Weapon_Main_Splattershot.png"),
    weapon("blaster", "https://cdn.wikimg.net/en/splatoonwiki/images/c/cc/S2_Weapon_Main_Blaster.png"),
    weapon("croller", "https://cdn.wikimg.net/en/splatoonwiki/images/8/8a/S2_Weapon_Main_Carbon_Roller.png"),
    weapon("roller", "https://cdn.wikimg.net/en/splatoonwiki/images/2/26/S2_Weapon_Main_Splat_Roller.png"),
    weapon("brush", "https://cdn.wikimg.net/en/splatoonwiki/images/thumb/c/c3/S2_Weapon_Main_Octobrush.png/64px-S2_Weapon_Main_Octobrush.png"),
    weapon("slosher", "https://cdn.wikimg.net/en/splatoonwiki/images/thumb/a/aa/S2_Weapon_Main_Slosher.png/64px-S2_Weapon_Main_Slosher.png"),
    weapon("dualies", "https://cdn.wikimg.net/en/splatoonwiki/images/thumb/d/de/S2_Weapon_Main_Splat_Dualies.png/64px-S2_Weapon_Main_Splat_Dualies.png"),
    weapon("brella", "https://cdn.wikimg.net/en/splatoonwiki/images/thumb/6/69/S2_Weapon_Main_Splat_Brella.png/64px-S2_Weapon_Main_Splat_Brella.png")
    ]
    random.shuffle(weapons)

    weaponUrl = weapons.pop()
    await ctx.send(weaponUrl.url)

@bot.command()
async def woomy(ctx):
    await ctx.send("https://www.youtube.com/watch?v=SE9pySihYpA")

@ bot.command()
async def agent8(ctx):
        await ctx.send("https://cdn.wikimg.net/en/splatoonwiki/images/5/57/Octo_Expansion_Marina%27s_Agent_8_drawing_-_compilation.png")
bot.run(TOKEN)
