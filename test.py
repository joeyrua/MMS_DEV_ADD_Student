import undetected_chromedriver as uc
import ddddocr
import time
from selenium.webdriver.common.keys import Keys

URL = uc.Chrome()
URL.maximize_window()

URL.get("https://tixcraft.com/ticket/ticket/24_jeffsatur/16446/1/75")

time.sleep(1)
accept = URL.find_element("xpath","/html/body/div[6]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/button")
accept.click()

time.sleep(1)
URL.execute_script("window.scrollBy(0,500)")

time.sleep(1)
select_number = URL.find_element("xpath","/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[1]/table/tbody/tr/td[2]/select")
select_number.click()

select_number.send_keys(Keys.DOWN)
select_number.send_keys(Keys.ENTER)

code = URL.find_element("xpath","/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[2]/div[2]/input")
imgCode = URL.find_element("xpath","/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[2]/div[1]/img")

time.sleep(1)
imgCode.screenshot("code.png")


ocr = ddddocr.DdddOcr()
with open("code.png","rb") as fp:
    image = fp.read()
catch = ocr.classification(image)
code.send_keys(catch)

code.send_keys(Keys.TAB,Keys.SPACE)

code.send_keys(Keys.ENTER)

