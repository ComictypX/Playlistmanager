#imports
import discord
import spotipy
import spotipy.util as util
import sys
import datetime
import yaml

from discord.ext import commands

#Settings
config = yaml.safe_load(open("config.yml"))

discordToken = config['DiscordAPI']['Token']
username = config['SpotifyUser']['username']
playlist_ID = config['SpotifyUser']['playlist_ID']
client_id = config['SpotifyAPI']['client_id']
client_secret = config['SpotifyAPI']['client_secret'] 

redirect_uri = "http://localhost:6969/callback" #Wo es nach der Nutzer Authentifizierung hingeht, am besten Host IP und Port angeben
scope = 'playlist-modify-private' #https://developer.spotify.com/documentation/general/guides/authorization/scopes/#playlist-modify-private

#Discord Setup
description = '''Ein Bot zum managen von Playlists'''
intents = discord.Intents.default()
activity=discord.Activity(type=discord.ActivityType.listening, name="Hardmelodies")
bot = commands.Bot(command_prefix='?', description=description, intents=intents, activity=activity)

#Spotify Setup
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
    sys.exit()

#Bot Logik

#Events
@bot.event
async def on_ready():
	print('Logged in as '+bot.user.name+' (ID:'+str(bot.user.id)+') | Connected to '+str(len(bot.guilds))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
	print('--------')
	print('Use this link to invite {}:'.format(bot.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=274877908992'.format(bot.user.id))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello there!')
    await bot.process_commands(message) #https://stackoverflow.com/questions/64692669/discord-bot-not-responding-to-commands-python    

#Commands
@bot.command(aliases=['+'])
async def add(ctx, *, tracks):
    """Fügt Lied zur Playlist hinzu"""
    #count Tracks in Playlist
    count_pre = sp.user_playlist_tracks(username, playlist_ID)['total']

    #Generate Track List
    track_list = tracks.split()

    #Log to Console
    print("Adding Track(s): ")
    print('\n'.join(map(str, track_list)))

    #Add Track(s) to Playlist
    sp.user_playlist_add_tracks(username, playlist_ID, track_list)

    #Count Tracks after change and build diff
    count_aft = sp.user_playlist_tracks(username, playlist_ID)['total']
    diff= count_aft - count_pre

    #send Message to context
    await ctx.send("Added " + str(diff) + " Track(s)")
    

@bot.command(aliases=['rem', 'del', '-'])
async def remove(ctx, *, tracks):
    """Emtfernt Lied von Playlist"""
    #count Tracks in Playlist
    count_pre = sp.user_playlist_tracks(username, playlist_ID)['total']

    #Generate Track List
    track_list = tracks.split()

    #Log to Console
    print("Removing Track(s): ")
    print('\n'.join(map(str, track_list)))
    
    #Remove Track(s) from Playlist
    sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_ID, track_list)

    #Count Tracks after change and build diff
    count_aft = sp.user_playlist_tracks(username, playlist_ID)['total']
    diff= -1*(count_aft - count_pre) # *-1 so the bot shows a positive number of removed tracks

    #send Message to context
    await ctx.send("Removed " + str(diff) + " Track(s)")

@bot.command()
async def info(ctx):
    """Gibt Informationen über den aktuellen Server"""
    embed = discord.Embed(title=f"{ctx.guild.name}", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")

    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    """Lässt den Bot mit pong antworten. Was hast du erwartet?"""
    await ctx.send('pong')        

#Sartet Bot
bot.run(discordToken)


