'''
This file finds the friend of the target person.
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
pos = int(input("Enter position: "))
repeat_time = int(input("Enter reapet time: "))

for i in range(repeat_time):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve name
    name = re.findall("_.+_(.+)\.html", url)
    name = name[0]

    # Retrieve all of the a tags
    tags = soup('a')
    try:
        url = tags[pos - 1].get("href", None)
        friend_name = re.findall("_.+_(.+)\.html", url)
        friend_name = friend_name[0]
        print(name + "'s", str(pos) + "th friend is", friend_name)
    except:
        print(name, "doesn't have so many friend. Sad.") 