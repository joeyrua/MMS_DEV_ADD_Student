import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = uc.Chrome()
URL.maximize_window()

wait = ui.WebDriverWait(URL,10)
action = ActionChains(URL)



#----登入帳密----

token = URL.execute_script('window.localStorage.getItem("token")')

js  = 'window.localSorage.setItem("token","token值")'
URL.execute_script(js)

URL.get("https://oneclub.backstage-dev.oneclass.com.tw/customer/customerlist")