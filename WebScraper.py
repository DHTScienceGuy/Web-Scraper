# -*- coding: utf-8 -*-
"""
Created on Wed May 19 03:03:39 2021

@author: The Art of DHT 
"""

import requests 
from bs4 import BeautifulSoup as bs 

dccomics_characters = input("input character: ")
url = "https://www.dccomics.com/characters"+dccomics_characters
r = requests.get(url)
soup = bs(r.content, "html.parser")
profile_image = soup.find("img", {"alt" : "Avatar"})["src"]
print(profile_image)

