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