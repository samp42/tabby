import datetime

class Tweet:
    author_name: str
    author_username: str
    datetime: datetime.datetime
    text: str
    num_likes: int
    num_views: int
    num_comments: int
    num_retweets: int


tweet = Tweet()
tweet.author_name = "John Doe"
tweet.author_username = "johndoe"
tweet.datetime = datetime.datetime(2023, 10, 1, 12, 0, 0)
tweet.text = "Hello, world!"
tweet.num_likes = 100
tweet.num_views = 1000
tweet.num_comments = 10
tweet.num_retweets = 1

import sys

a = 5
b:int = 10
c:str = ""

print(sys.getsizeof(tweet))
print(sys.getsizeof(tweet.datetime))
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print("---")
print(tweet.__sizeof__())
print(tweet.datetime.__sizeof__())
print(a.__sizeof__())
print(b.__sizeof__())
print(c.__sizeof__())
