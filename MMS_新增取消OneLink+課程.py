import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

URL = uc.Chrome()
wait = ui.WebDriverWait(URL,10)
action = ActionChains(URL)

URL.maximize_window()
URL.get("https://oneclub.backstage-dev.oneclass.com.tw/")

#----登入MMS帳密----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[1]/div/input"))
account = URL.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[1]/div/input")
account.send_keys("ONE50397")#帳號

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[2]/div/input"))
password = URL.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[2]/div/input")
password.send_keys("juan7890")#密碼

password.send_keys(Keys.ENTER)#打完帳密按下Enter

time.sleep(1)
wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[1]"))
member_manage = URL.find_element("xpath","/html/body/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[1]")
member_manage.click()#會員管理

time.sleep(1)
wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[3]"))
learning_course_manage = URL.find_element("xpath","/html/body/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[3]")
learning_course_manage.click()#補教課程管理

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[4]"))
general_course_manage = URL.find_element("xpath","/html/body/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[4]")
general_course_manage.click()#一般課程管理

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div/div[2]/button"))
add_course = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div/div[2]/button")
add_course.click()#新增課程

wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div[2]/div[3]/div[2]/button[2]"))
choose_OneLinkPlus_btn = URL.find_element("xpath","/html/body/div[2]/div[3]/div[2]/button[2]")
choose_OneLinkPlus_btn.click()#選擇OneLink+課程

URL.switch_to.window(URL.window_handles[1])#切換到另一個分頁


wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div[2]/div/div/div/input"))
input_institution_name = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div[2]/div/div/div/input")
input_institution_name.send_keys("測試全補習班")#輸入機構名稱
input_institution_name.send_keys(Keys.DOWN)
input_institution_name.send_keys(Keys.ENTER)

URL.execute_script("window.scrollBy(0,500)")

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[3]/div[2]/div/div/div/input"))
branch_school = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[3]/div[2]/div/div/div/input")
branch_school.send_keys(Keys.DOWN)#分校
branch_school.send_keys(Keys.DOWN)
branch_school.send_keys(Keys.ENTER)

time.sleep(1)
wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[4]/div[2]/div/div/div/input"))
classroom = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[4]/div[2]/div/div/div/input")
classroom.send_keys(Keys.DOWN)
classroom.send_keys(Keys.DOWN)
classroom.send_keys(Keys.ENTER)#班級

URL.execute_script("window.scrollBy(0,400)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div[2]/div/div/button"))
course_date = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div[2]/div/div/button")
course_date.click()#課程日期

time.sleep(1)
wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div[5]/div[2]/button"))
choose_date = URL.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div[5]/div[2]/button")
choose_date.click()

wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[3]/div[2]/div/input"))
start_time = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[3]/div[2]/div/input")
start_time.send_keys("1400")#開始時間

URL.execute_script("window.scrollBy(0,400)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/input"))
course_label = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/input")
course_label.send_keys(Keys.DOWN)
course_label.send_keys(Keys.DOWN)
course_label.send_keys(Keys.ENTER)

black = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[3]/div[1]")
black.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[3]/div[2]/div[2]/div/div/input"))
choose_teacher = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[3]/div[2]/div[2]/div/div/input")
choose_teacher.send_keys("黃分氣")
choose_teacher.send_keys(Keys.DOWN)
choose_teacher.send_keys(Keys.ENTER)


wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/input"))
course_name=URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/input")
course_name.send_keys("測試OneLink+補習班")

wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/input"))
post_btn = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div/div[2]/button[3]")
post_btn.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div/div[2]/button[1]"))
channel = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div/div[2]/button[1]")
channel.click()

choose_institution_name = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div/div[2]/div[2]/div/div/input")
choose_institution_name.send_keys("測試全補習班")
choose_institution_name.send_keys(Keys.ENTER)

