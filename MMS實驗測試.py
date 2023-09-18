import selenium.webdriver.support.ui as ui
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

URL = uc.Chrome()
wait = ui.WebDriverWait(URL,10)
action = ActionChains(URL)

URL.maximize_window()
URL.get("https://oneclub.backstage-dev.oneclass.com.tw/")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[1]/div/input"))
account = URL.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[1]/div/input")
account.send_keys("ONE50397")#帳號

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[2]/div/input"))
password = URL.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[2]/div/input")
password.send_keys("juan7890")#密碼

password.send_keys(Keys.ENTER)#打完帳密按下Enter

time.sleep(5)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[2]/main/div[2]/div[3]/div[1]/div"))
choose_field = URL.find_element("xpath","/html/body/div[1]/div[2]/main/div[2]/div[3]/div[1]/div")
choose_field.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[3]/ul/li[2]"))
choose_field_2 = URL.find_element("xpath","/html/body/div[2]/div[3]/ul/li[2]")
choose_field_2.click()