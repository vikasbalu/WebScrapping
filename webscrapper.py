import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
url = 'https://github.com/'+github_user #from which url we are scarpping 

r = requests.get(url) # send request to that url 

soup = bs(r.content, 'html.parser') # soup is used to scrap the website
#print(soup.prettify()) # this will print whole html content of the webpage in a prettified format

# Open a file for writing ('w' stands for write)
with open('output.txt', 'w') as file:
    # Write content to the file
    file.write(soup.prettify())

print('Content has been written to the file.')


profile_image = soup.find('img')['src']

#print(profile_image)




