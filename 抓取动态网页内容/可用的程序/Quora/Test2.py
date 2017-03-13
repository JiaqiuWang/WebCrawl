from urllib.request import urlopen
import json
from pprint import pprint

u = urlopen('https://tch823564.tch.quora.com/up/chan32-8888/updates?min_seq=4276119137&channel=main-w-dep3004-4287'
            '42902611017586&hash=9683997917737376104&callback=jsonp15a09e025f91dad7b36e8313')
content = u.read()
print("content:", content)
resp = json.loads(u.read().decode('utf-8'))
pprint("resp:", resp)
