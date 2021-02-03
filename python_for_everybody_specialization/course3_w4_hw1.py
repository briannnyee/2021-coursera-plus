from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
cnt = 0
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('class:', tag.get('class', None))
    print('Contents:', tag.contents[0])
    cnt += int(tag.contents[0])
print("Sum:", cnt)