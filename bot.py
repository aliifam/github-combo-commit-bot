from selenium import webdriver
from datetime import date
import datetime

#maybe this chromdriver not have same version as your chrome browser you can download and change the app in chromedriver.exe

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)

def commit():
    driver.get("https://github.com/login")

    email = "YOUR USERNAME" #replace the username as your github username
    password = "YOUR PASSWORD" #repalce the password as your github password
    now = datetime.datetime.now()
    d2 = now.strftime("%d/%m/%Y %H:%M:%S")

    driver.find_element_by_id('login_field').send_keys(email)
    driver.find_element_by_id('password').send_keys(password)

    driver.find_element_by_name('commit').click();

    driver.get("https://github.com/edufest/manipulate-active/edit/main/README.md") #replace the link as you want 

    driver.find_element_by_css_selector('.CodeMirror-wrap pre.CodeMirror-line').send_keys("✔️ Fake Bot Commit ============ ", d2, "\n", "\n")

    driver.find_element_by_id('commit-summary-input').send_keys("commit in: ", d2)

    driver.find_element_by_id('submit-file').click();

    driver.quit()

commit();
