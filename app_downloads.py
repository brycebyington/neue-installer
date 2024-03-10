import requests
import os

def download_spotify():
    url = 'https://download.scdn.co/SpotifySetup.exe'
    r = requests.get(url, allow_redirects=True)
    open('SpotifySetup.exe', 'wb').write(r.content)
    os.startfile("SpotifySetup.exe")
    pass

def download_vscode():
    url = 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user'
    r = requests.get(url, allow_redirects=True)
    open('VSCodeSetup.exe', 'wb').write(r.content)
    os.startfile("VSCodeSetup.exe")
    pass

def download_vlc():
    url = 'https://mirror.fcix.net/videolan-ftp/vlc/3.0.20/win64/vlc-3.0.20-win64.exe'
    r = requests.get(url, allow_redirects=True)
    open('vlc-3.0.20-win64', 'wb').write(r.content)
    os.startfile("vlc-3.0.20-win64")
    pass