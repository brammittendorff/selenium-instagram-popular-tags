import os
import sys
import time
import random
import argparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

parser = argparse.ArgumentParser(description='Instagram Popular Tags')
parser.add_argument('-w', '--word', help='a word to lookup on instagram', nargs='?')

args = parser.parse_args()

def write_to_json(response_data, word):
    if response_data:
        myfile = 'wordpages/' + word + '.json'
        if not os.path.isfile(myfile):
            strip1 = response_data.split(r'window._sharedData = ')
            if len(strip1) > 1:
                strip2 = strip1[1].split(r";</script>")
                if len(strip2) > 0:
                    with open(myfile, "w") as outfile:
                        outfile.write(strip2[0])

if args.word:
    capabilities = webdriver.common.desired_capabilities.DesiredCapabilities.CHROME.copy()
    capabilities['javascriptEnabled'] = True
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/75.0.3770.90 Chrome/75.0.3770.90 Safari/537.36')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities,
        options=options
    )
    
    current_session = driver.session_id

    driver.get('https://www.instagram.com/explore/tags/{}/'.format(args.word))

    write_to_json(driver.page_source, args.word)

    driver.quit()
