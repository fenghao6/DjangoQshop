from django.test import TestCase
from time import sleep
from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get("https://www.baidu.com")
# chrome.find_element_by_id("kw").send_keys("qq空间")
# chrome.find_element_by_id("su").click()
# chrome.find_element_by_id("img_out_3392279511").click()
sleep(5)
chrome.close()
# Create your tests here.
