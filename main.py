from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

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
    header = browser.find_element(By.CLASS_NAME, "header-cell").text.split("\n")
    title = header[0]
    name = header[1][4:]
    time = browser.find_element(By.CLASS_NAME, "times-cell").text.split(" ")
    date = time[0]
    start = time[1]
    stop = time[3]
    description = browser.find_element(By.CLASS_NAME, "sc-bjUoiL.sc-hjriPb.jracsp.cktPVE").text
    pass

browser.close()
