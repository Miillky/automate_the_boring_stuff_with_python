#!/usr/bin python3

# Automatically plays the game 2048.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://play2048.co/')
html_elem = browser.find_element_by_tag_name('html')

while True:
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)