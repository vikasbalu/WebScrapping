import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input Github User: ")
url = "https://github.com/"+github_user #from which url we are scarpping 

r = requests.get(url) # send request to that url 

soup = bs(r.content, 'html.parser') # soup is used to scrap the website

profile_image = soup.find('img', {'alt': 'Avatar'})['src']

print(profile_image)



