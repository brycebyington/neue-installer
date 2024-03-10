import requests
import os

def download_chrome():
    url = 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B174A7620-9415-9D99-657A-9BC9A55F025F%7D%26lang%3Den%26browser%3D4%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DFDET%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe'
    r = requests.get(url, allow_redirects=True)

    open('ChromeSetup.exe', 'wb').write(r.content)
    os.startfile("ChromeSetup.exe")
    pass

def download_firefox():
    url = 'https://download-installer.cdn.mozilla.net/pub/firefox/releases/123.0.1/win32/en-US/Firefox%20Installer.exe'
    r = requests.get(url, allow_redirects=True)
    open('Firefox%20Installer.exe', 'wb').write(r.content)
    os.startfile("Firefox%20Installer.exe")
    pass