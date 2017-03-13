import urllib.request as urt
req = urt.Request('http://www.example.com/')
req.add_header('Referer', 'http://www.python.org/')
r = urt.urlopen(req)
print(r.read())
