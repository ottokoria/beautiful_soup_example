# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests


web_address = "http://tripitaka.cbeta.org/zh-cn/T52n2104_004"

# connect to the webpage
web_response = requests.get(web_address)

# scrape the specific information
the_soup_object = BeautifulSoup(web_response.text)

list_tags = the_soup_object.find_all("li")

# print out the information we care about
for tag in list_tags:
    print(tag.text * 2)
