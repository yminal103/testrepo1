import os

print('Jenkins credentials')

username = os.getenv('username')
password = os.getenv('Password')

print('Username', username)
print('Password', password)
