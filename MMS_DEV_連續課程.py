import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pickle

URL = uc.Chrome()
URL.maximize_window()
wait = ui.WebDriverWait(URL,10)
action = ActionChains(URL)

URL.get("https://oneclub.backstage-dev.oneclass.com.tw/login")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/input"))
input_account = URL.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/input")
input_account.send_keys("ONE50397")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/input"))
input_password = URL.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/input")
input_password.send_keys("juan7890")
input_password.send_keys(Keys.ENTER)

time.sleep(3)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[1]"))
member_management = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[1]")
member_management.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[2]"))
Curriculum_management = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[2]")
Curriculum_management.click()


time.sleep(1)
wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[3]/div/div/div/a[6]"))
Continuous_Curriculum_management = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[3]/div/div/div/a[6]")
Continuous_Curriculum_management.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/button[2]"))
add_Continuous_Curriculum = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/button[2]")
add_Continuous_Curriculum.click()

URL.switch_to.window(URL.window_handles[1])#切換到另一個分頁

time.sleep(3)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div/div/input"))
input_oneclub_id = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div/div/input")
input_oneclub_id.send_keys("green004")

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[2]/div/div/div/div/input"))
input_studnet_name = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[2]/div/div/div/div/input")
input_studnet_name.send_keys("林新月")
input_studnet_name.send_keys(Keys.DOWN)
input_studnet_name.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[3]/div/div[2]/div/div/div/input"))
input_course_type = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[3]/div/div[2]/div/div/div/input")
input_course_type.send_keys("國小正式25分鐘")
input_course_type.send_keys(Keys.DOWN)
input_course_type.send_keys(Keys.ENTER)

URL.execute_script("window.scrollBy(0,600)")

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/button"))
first_date = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/button")
first_date.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div[2]/button"))
Feb_Twelth = URL.find_element("xpath","/html/body/div[5]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div[2]/button")
Feb_Twelth.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/button"))
end_date = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/button")
end_date.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[2]/div/div/div/div[2]/div/div[2]/div/div[4]/div[7]/button"))
Feb_Twenty_Fourth = URL.find_element("xpath","/html/body/div[5]/div[2]/div/div/div/div[2]/div/div[2]/div/div[4]/div[7]/button")
Feb_Twenty_Fourth.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[1]/div/div/div"))
choose_day = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[1]/div/div/div")
choose_day.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[3]/ul/li[2]"))
Monday = URL.find_element("xpath","/html/body/div[5]/div[3]/ul/li[2]")
Monday.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[2]/div/div/input"))
input_time_btn = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[2]/div/div/input")
input_time_btn.click()

#URL.switch_to.window(URL.window_handles[2])#切換到另一個分頁


