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

wait.until(lambda driver:driver.find_element("xpath","(.//*[normalize-space(text()) and normalize-space(.)='general v1.0.0'])[1]/following::div[1]"))
member_manage = URL.find_element("xpath","(.//*[normalize-space(text()) and normalize-space(.)='general v1.0.0'])[1]/following::div[1]")
member_manage.click()

time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","(.//*[normalize-space(text()) and normalize-space(.)='會員管理'])[1]/following::div[1]"))
Curroclum_Management = URL.find_element("xpath","(.//*[normalize-space(text()) and normalize-space(.)='會員管理'])[1]/following::div[1]")
Curroclum_Management.click()

#----新增正式課----
time.sleep(1)
wait.until(lambda driver:driver.find_element("xpath","(.//*[normalize-space(text()) and normalize-space(.)='試聽課程管理'])[1]/following::div[2]"))
general_course = URL.find_element("xpath","(.//*[normalize-space(text()) and normalize-space(.)='試聽課程管理'])[1]/following::div[2]")
general_course.click()#正式課

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div/div[3]/button"))
add_general_course = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div/div[3]/button")
add_general_course.click()#新增課程

URL.switch_to.window(URL.window_handles[1])#切換到另一個分頁

time.sleep(2)
URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/div/div/input"))
input_oneclub_id = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/div/div/input")
input_oneclub_id.send_keys("green004")#輸入學生Oneclub_id

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div/div/div/input"))
choose_student_name = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div/div/div/input")
choose_student_name.click()#選擇學生
time.sleep(3)
choose_student_name.send_keys(Keys.DOWN)
choose_student_name.send_keys(Keys.ENTER)

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[3]/div[2]/div/div/div/input"))
course_type = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[3]/div[2]/div/div/div/input")
course_type.click()#選擇課程類別
course_type.send_keys("國小")
course_type.send_keys(Keys.DOWN)
course_type.send_keys(Keys.ENTER)

wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div[2]/div/div/button"))
course_date = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div[2]/div/div/button")
course_date.click()

wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div[5]/div[4]/button"))
jan_tw_five = URL.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div[5]/div[4]/button")
jan_tw_five.click()


wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div[1]/div[2]/main/div[2]/div[3]/div[3]/div[2]/div/div/button"))
clock_btn = URL.find_element("xpath","/html/body/div[1]/div[2]/main/div[2]/div[3]/div[3]/div[2]/div/div/button")
clock_btn.click()

time.sleep(2)
wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/span[12]"))
eleven = URL.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/span[12]")
action.move_to_element(eleven).click().perform()

time.sleep(1)
wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[4]/span[6]"))
half = URL.find_element("xpath","/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[4]/span[6]")
action.move_to_element(half).click().perform()


URL.execute_script("window.scrollBy(0,600)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/input"))
choose_course_lable = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/input")
choose_course_lable.click()#選擇課程標籤
choose_course_lable.send_keys(Keys.DOWN)
choose_course_lable.send_keys(Keys.ENTER)

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[3]/div[2]/div[2]/div/div/input"))
choose_teacher = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[3]/div[2]/div[2]/div/div/input")
ActionChains(URL).move_to_element(choose_teacher).click().perform()#選擇老師
for i in range(2):
    choose_teacher.send_keys(Keys.DOWN)
choose_teacher.send_keys(Keys.ENTER)

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[4]/div[2]/div/div/div/input"))
choose_library = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[4]/div[2]/div/div/div/input")
choose_library.click()#選擇叢書
for i in range(9):
    choose_library.send_keys(Keys.DOWN)
choose_library.send_keys(Keys.ENTER)

time.sleep(2)
URL.execute_script("window.scrollBy(0,600)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/input"))
input_course_name = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/input")
input_course_name.send_keys("happy_course")#輸入課程名稱

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[3]/div[2]/div/textarea[1]"))
teach_remind = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[3]/div[2]/div/textarea[1]")
teach_remind.send_keys("aaaa")#輸入授課提醒

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div/div[2]/button[3]"))
post = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div/div[2]/button[3]")
post.click()#按下發布

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div/div[2]/div[2]/div/div/input"))
choose_input_student_name = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div/div[2]/div[2]/div/div/input")
choose_input_student_name.send_keys("林新月")
choose_input_student_name.send_keys(Keys.ENTER)

URL.execute_script("window.scrollBy(0,300)")

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/table/tbody/tr/td[9]/div/div/button"))
edit = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/table/tbody/tr/td[9]/div/div/button")
edit.click()

URL.switch_to.window(URL.window_handles[2])#切換到另一個分頁

wait.until(lambda drvier:drvier.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[9]/div/div[1]"))
channel_course = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[9]/div/div[1]")
channel_course.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[3]/div/div/div[1]/div[4]/div/textarea[1]"))
input_change_reason = URL.find_element("xpath","/html/body/div[2]/div[3]/div/div/div[1]/div[4]/div/textarea[1]")
input_change_reason.send_keys("abcd1234")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[3]/div/div/div[2]/button[2]"))
confirm_channel = URL.find_element("xpath","/html/body/div[2]/div[3]/div/div/div[2]/button[2]")
confirm_channel.click()







