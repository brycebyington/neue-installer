import requests
import os

def download_steam():
    url = 'https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe'
    r = requests.get(url, allow_redirects=True)

    open('SteamSetup.exe', 'wb').write(r.content)
    os.startfile("SteamSetup.exe")
    pass

def download_discord():
    url = 'https://dl.discordapp.net/distro/app/stable/win/x86/1.0.9035/DiscordSetup.exe'
    r = requests.get(url, allow_redirects=True)
    
    open('DiscordSetup.exe', 'wb').write(r.content)
    os.startfile("DiscordSetup.exe")
    pass