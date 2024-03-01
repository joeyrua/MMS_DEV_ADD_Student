import undetected_chromedriver as uc
import ddddocr
import time
from selenium.webdriver.common.keys import Keys

URL = uc.Chrome()
URL.maximize_window()

URL.get("https://tixcraft.com/activity/detail/24_mayday")

time.sleep(1)
accept = URL.find_element("xpath","/html/body/div[6]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/button")
accept.click()

time.sleep(1)
URL.execute_script("window.scrollBy(0,500)")

time.sleep(1)
Immediate_ticket = URL.find_element("xpath","/html/body/div[2]/div[1]/section[2]/div/div[1]/div/ul/li[1]")
Immediate_ticket.click()

time.sleep(1)
choose_date = URL.find_element("xpath","/html/body/div[2]/div[1]/section[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[4]/button")
choose_date.click()

time.sleep(1)
URL.execute_script("window.scrollBy(0,500)")

time.sleep(1)
choose_price_and_area = URL.find_element("xpath","/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/ul[2]/li[2]")
choose_price_and_area.click()

time.sleep(1)
select_number = URL.find_element("xpath","/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[1]/table/tbody/tr/td[2]/select")
select_number.click()

for i in range(4):
    select_number.send_keys(Keys.DOWN)
select_number.send_keys(Keys.ENTER)

time.sleep(1)
URL.execute_script("window.scrollBy(0,300)")

code = URL.find_element("xpath","/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[2]/div[2]/input")
imgCode = URL.find_element("xpath","/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[2]/div[1]/img")

time.sleep(1)
imgCode.screenshot("code.png")


ocr = ddddocr.DdddOcr()
with open("code.png","rb") as fp:
    image = fp.read()
catch = ocr.classification(image)
code.send_keys(catch)

time.sleep(3)
code.send_keys(Keys.TAB,Keys.SPACE)

code.send_keys(Keys.ENTER)

google_login = URL.find_element("xpath","/html/body/div[2]/section/div/div[2]/div[2]/a")
google_login.click()

time.sleep(1)
google_account = URL.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
google_account.send_keys("yellow145258789")
google_account.send_keys(Keys.ENTER)

time.sleep(2)
google_password = URL.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
google_password.send_keys("juan145258789145258789145258789")
google_password.send_keys(Keys.ENTER)

time.sleep(2)
verify = URL.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/section/div/div/div/ul/li[2]")
verify.click()
