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

def download_epic_games_launcher():
    url = 'https://download1.epicgames.com/Builds/UnrealEngineLauncher/Windows/EpicGamesLauncher.exe'
    r = requests.get(url, allow_redirects=True)

    open('EpicInstaller-15.17.1', 'wb').write(r.content)
    os.startfile("EpicInstaller-15.17.1.exe") 
    # Will need to be able to handle versions getting updated in the future, I may cache downloads in S3 possibly?
    pass