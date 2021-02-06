import urllib.request
import json

url = 'http://py4e-data.dr-chuck.net/comments_1152458.json'
uh = urllib.request.urlopen(url)

data = uh.read().decode()
json_data = json.loads(data)
comments = json_data['comments']

count_sum = 0
for comment in comments:
    count_sum += int(comment['count'])
print(count_sum)