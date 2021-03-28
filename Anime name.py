import requests
import random
from bs4 import BeautifulSoup

url = "https://myanimelist.net/character.php"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html5lib")
links = soup.findAll("a")

first_name = []
last_name = []
un_sortd_names = []

for link in links:
    href = link.get('href')
    if type(href) == str and '/character/' in href and href not in un_sortd_names:
        un_sortd_names.append(href)

for i in un_sortd_names:
    n = i.split("/")
    s = n[-1].split("_")
    first_name.append(s[0])
    if (len(s) > 1):
        last_name.append(s[1])

n = True

while (n == True):

    first = random.randint(0, len(first_name))
    last = random.randint(0, len(last_name))

    print("Your random anime name is: ", first_name[first], last_name[last])

    go_again = input("would you like to go again? Y/N ")
    if (go_again == "N"):
        n = False
