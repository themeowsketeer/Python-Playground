import requests as req
from bs4 import BeautifulSoup as bs

github_user = input('Input a Github user: ')

url = 'https://github.com/' + github_user

request = req.get(url)

soup = bs(request.content, 'html.parser')

profile_image = soup.find('img', {'alt': 'Avatar'})['src']

print(profile_image)