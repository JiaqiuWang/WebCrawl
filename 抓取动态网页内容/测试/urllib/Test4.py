import urllib.request as urt

opener = urt.build_opener()
opener.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, "
                                    "like Gecko) Chrome/55.0.2883.87 Safari/537.36")]
opener.addheaders = [('Cookie', "guest_id=v1%3A148482531768369694; mobile_metrics_token=148482538426969560; zrca=5; "
                                "pid=\"v3:1484832195137856638274668\"; " \
                                "_mobile_sess=BAh7ByIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZ" \
                                "sYXNoSGFzaHsABjoKQHVzZWR7ADoQX2NzcmZfdG9rZW4iJTViMjY1NTAwMmQzYjc5MDk5" \
                                "ZTUyMjg2ZDRmODRlMzI1--d47c9fabb6613c0b8a0e6c8d54e31ae533dc631a; " \
                                "_gat=1; kdt=um9UDXk2qUARHElvAh5qyd7unesk6QvMLYPverbd; " \
                                "remember_checked_on=1; twid=\"u=819088284554907648\"; " \
                                "auth_token=ca6eceb576dc4df26bebe081fc11fb9f773962e5; lang=zh-cn;" \
                                " _ga=GA1.2.1762403604.1484825327; " \
                                "_twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6" \
                                "OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCP8u5blZAToMY3N" \
                                "yZl9p%250AZCIlMzFiZWRlMDViZGNhYmY5YTNkOWEwZDk2NTJlNTQxOWU6B2lkIiVjMz" \
                                "c3%250AMmRmZjBmNjhlMjJmZWY1YjRkMWFiOWYyZjhiODoJdXNlcmwrCQBQlIB0%25" \
                                "2FF0L--4650ca63a9eca887a5ac096ad250735fa2b5ca7e")]
page = opener.open('https://twitter.com/i/profiles/show/poke/timeline/'
                   'with_replies?include_available_features=1&include_entities=1&'
                   'max_position=817384951360487426&reset_error_state=false')
print("page:", page.read())
# print("type-page:", type(page))
