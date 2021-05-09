from selenium import webdriver
import time
import urllib
import urllib3

x="youtu.be/y1ZPcM7IMP8"


refreshrate= 30
refreshrate=int(refreshrate)
driver =  webdriver.Firefox()
driver.get("http://"+x)

while True:
    time.sleep(refreshrate)
    driver.refresh()
