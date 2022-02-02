# PlaylistManager
A Discord Bot to manage a pre configured private Playlist

## Installation
1. clone repo `git clone https://github.com/ComictypX/Playlistmanager.git`
2. Install [Spotipy](https://github.com/plamere/spotipy)
`python3 -m pip  install spotipy --upgrade`
3. Install [Discord.py](https://github.com/Rapptz/discord.py)
`python3 -m pip install -U discord.py`

## Setup
1. copy config.yml.sample `cp config.yml.sample config.yml`
2. Create a Discord Bot Account [Creating a Bot Account](https://discordpy.readthedocs.io/en/stable/discord.html)
   - Copy token into config.yml > DiscordAPI > Token
3. Create a Spotify Application [My Dashboard](https://developer.spotify.com/dashboard/applications)
   - Enter Client ID and Client Secrete into config.yml > SpotifyAPI
   - Add `http://localhost:6969/callback` as Redirect URI in your Spotify Applications Settings
   - Add your Spotify Account under "Users and Access"
4. Configure your Spotify Username and Playlist in config.yml > SpotifyUser
   - How to get user ID: Share your Profile. The id is after `http://open.spotify.com/user/`
   - Hot wo get Playlist ID: Share Playlist. The id is after `https://open.spotify.com/playlist/`
5. run main.py
6. Follow Instructions in Bot console to add Bot to Server

## Bot usage
Bot commands start with ?<command>

Output ?help:
```
Ein Bot zum Verwalten von Playlists

No Category:
  add    Fügt Lied zur Playlist hinzu
  help   Shows this message
  info   Gibt Informationen über den aktuellen Server
  link   Gibt Link der Verwalteten Playlist zurück
  ping   Lässt den Bot mit pong antworten. Was hast du erwartet?!
  remove Emtfernt Lied von Playlist

Type ?help command for more info on a command.
You can also type ?help category for more info on a category.
```

## Todo
- Permission-System (Who should be able to use Bot)
- ability to limit bot to specific channels
