"""100 greatest hollywood movies"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2", timeout=20)

html_data = BeautifulSoup(response.text, "html.parser")

movies_header = html_data.select("span h2 strong")
movies_header.reverse()

movies_list = [header.getText() for header in movies_header]
for header in movies_header:
    print(header.getText())
