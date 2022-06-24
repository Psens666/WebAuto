from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep

from selenium.webdriver.chrome.options import Options

#options = Options()
#options.add_argument("--headless")
#options.add_argument("--disable-gpu")

courses = [
    "https://app.kursifant.com/courses/6290bc9413cab319c291a080",
    "https://app.kursifant.com/courses/62ab2ab9e95de3636db7f9b6",
    "https://app.kursifant.com/courses/62ab2ba8e95de3636db8d64e"
]

browser = Chrome('C:\\Users\\Dominic Lang\\chromedriver_win32\\chromedriver.exe')
browser.implicitly_wait(10)
browser.get("https://app.kursifant.com/login")

email = browser.find_element(By.NAME, "email")
passwd = browser.find_element(By.NAME, "password")
email.send_keys("dominic.lang@kaspauer.de")
passwd.send_keys("Lemmy2022")
passwd.submit()



for course in courses:
    browser.get(course)
    header = browser.find_element(By.CLASS_NAME, "header-cell")
    print(header.text)
    zeit = browser.find_element(By.CLASS_NAME, "times-cell")
    print(zeit.text)
    #divs = browser.find_elements(By.TAG_NAME, "div")
    #for div in divs:
    #    print(div.get_attribute("class"))
    beschreibung = browser.find_element(By.CLASS_NAME, "sc-bjUoiL.sc-hjriPb.jracsp.cktPVE")
    print(beschreibung.text)
    sleep(10)

browser.close()
