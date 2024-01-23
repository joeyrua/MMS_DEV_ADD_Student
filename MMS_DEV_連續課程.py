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

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[1]/div/input"))
input_account = URL.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[1]/div/input")
input_account.send_keys("ONE50397")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[2]/div/input"))
input_password = URL.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[2]/div/input")
input_password.send_keys("juan7890")
input_password.send_keys(Keys.ENTER)

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div/div[2]"))
member_management = URL.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div/div[2]")
member_management.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div[2]"))
Curriculum_management = URL.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div[2]")
Curriculum_management.click()

time.sleep(1)
wait.until(lambda drvier:drvier.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div[3]/div/div/div/a[6]/div[2]"))
Continuous_Curriculum_management = URL.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div[3]/div/div/div/a[6]/div[2]")
Continuous_Curriculum_management.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/button[2]"))
add_Continuous_Curriculum = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/button[2]")
add_Continuous_Curriculum.click()

URL.switch_to.window(URL.window_handles[1])#切換到另一個分頁

wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div/div/input"))
input_oneclub_id = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div/div/input")
input_oneclub_id.send_keys("green004")

time.sleep(3)
wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[2]/div/div/div/div/input"))
input_student_name  = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[2]/div/div/div/div/input")
input_student_name.click()
input_student_name.send_keys(Keys.DOWN)
input_student_name.send_keys(Keys.ENTER)

wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div[3]/div/div[2]/div/div/div/input"))
input_course_type = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div[3]/div/div[2]/div/div/div/input")
input_course_type.send_keys("國小正式25分鐘")
input_course_type.send_keys(Keys.DOWN)
input_course_type.send_keys(Keys.ENTER)

URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div[1]/div[2]/main/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/button"))
first_time = URL.find_element("xpath","/html/body/div[1]/div[2]/main/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/button")
first_time.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/button[2]"))
next_monuth = URL.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/button[2]")
next_monuth.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div[5]/button"))
Feb_one = URL.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div[5]/button")
Feb_one.click()#開始時間

time.sleep(1)
wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/button"))
end_time = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/button")
end_time.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/button[2]"))
next_monuth = URL.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/button[2]")
next_monuth.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div[5]/button"))
Feb_fourteen = URL.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div[5]/button")
Feb_fourteen.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div/div"))
choose_day = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div/div")
choose_day.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[3]/ul/li[2]"))
Monday = URL.find_element("xpath","/html/body/div[2]/div[3]/ul/li[2]")
Monday.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/button"))
time_clock = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/button")
time_clock.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/span[11]"))
ten_clock = URL.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/span[11]")
action.move_to_element(ten_clock).click().perform()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[4]/span[6]"))
half = URL.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[4]/span[6]")
action.move_to_element(half).click().perform()

URL.execute_script("window.scrollBy(0,300)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div[2]/div[2]/div/div/div/input"))
select_course_label = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div[2]/div[2]/div/div/div/input")
select_course_label.click()
select_course_label.send_keys(Keys.DOWN)
select_course_label.send_keys(Keys.ENTER)

time.sleep(1)
black = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[1]")
black.click()

select_teacher = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[3]/div/div[2]/div/div[1]/div[1]/div/div/div/input")
select_teacher.send_keys("黃分氣")
time.sleep(2)
select_teacher.send_keys(Keys.DOWN)
select_teacher.send_keys(Keys.ENTER)

post_btn = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div/button[2]")
post_btn.click()

time.sleep(3)

eye = URL.find_element("xpath","/html/body/div/div[2]/main/div[3]/table/tbody/tr[3]/td[6]/button")
eye.click()

URL.switch_to.window(URL.window_handles[2])#切換到另一個分頁
time.sleep(2)
cancel = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div/button[1]")
cancel.click()

confirm_click= URL.find_element("xpath","/html/body/div[2]/div[3]/div/div/div[2]/button[2]")
confirm_click.click()


back_btn = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div/button[2]")
back_btn.click()
