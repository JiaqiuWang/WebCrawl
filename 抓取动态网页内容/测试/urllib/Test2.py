import urllib.request as urt
req = urt.Request('https://twitter.com/poke/with_replies')
response = urt.urlopen(req)
the_page = response.read()
print("page:", the_page)
