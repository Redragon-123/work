"""
Task 2.2: Send Data Using POST Requests

Goal: Learn to send data to an API using POST requests.

Exercises:
- Create a new post
- Add a new comment to a post
- Create a new user
"""

import httpx

# Exercise 2.1: Create a new post
url = "https://jsonplaceholder.typicode.com/posts"
# TODO: Define new post data and send POST request
new_post=1
response=httpx.post(url, json=new_post)
if response.status_code==201:
    print("Post create successfully!")
    print(response.json())


# Exercise 2.2: Add a new comment to a post
url = "https://jsonplaceholder.typicode.com/comments"
# TODO: Define new comment data and send POST request
new_comment=1
response=httpx.post(url,new_comment)
if response.status_code==201:
    print("Post create successfully!")
    print(response.json())
# Exercise 2.3: Create a new user
url = "https://jsonplaceholder.typicode.com/users"
# TODO: Define new user data and send POST request
new_user=1
response=httpx.post(url,new_user)
if response.status_code==201:
    print("Post create successfully!")
    print(response.json())