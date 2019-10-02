import os
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

timeout = 1

load_dotenv()

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

driver.get('https://google.com')

driver.save_screenshot("screenshots/screenshot_%s.png" % current_session)

driver.quit()
