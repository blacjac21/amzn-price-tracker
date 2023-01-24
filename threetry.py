from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from selectorlib import Extractor
from tracker import (
    get_web_driver_options,
    get_chrome_web_driver,
    set_ignore_certificate_error,
    set_browser_as_incognito,
    set_automation_as_head_less,)
import requests
import json
import time

def search_amazon(item):

    options = get_web_driver_options() # setting options in selinium browser
        # set_automation_as_head_less(options) 
    set_ignore_certificate_error(options)
    set_browser_as_incognito(options)
    driver = get_chrome_web_driver(options)
    driver.get('https://www.amazon.in')
    search_box = driver.find_element(By.ID,'twotabsearchtextbox').send_keys(item)
    search_button = driver.find_element(By.ID,"nav-search-submit-text").click()

    driver.implicitly_wait(5)

    e = Extractor.from_yaml_file('search_results.yml')
    data = e.extract(driver.page_source)

    
    with open('search_results_output.jsonl','w') as outfile:
        if data:
            for product in data['products']:
                #product['search_url'] = url
                print("Saving Product: %s"%product['price'])
                json.dump(product,outfile)
                outfile.write("\n")
                # sleep(5)


if __name__ == '__main__':
    search_amazon('nvme ssd 500gb')