import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

URL= uc.Chrome()
URL.maximize_window()

wait = ui.WebDriverWait(URL,10)
action = ActionChains(URL)

URL.get("https://oneclub.backstage-dev.oneclass.com.tw/")

#----登入MMS帳密----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[1]/div/input"))
account = URL.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[1]/div/input")
account.send_keys("ONE50397")#帳號

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[2]/div/input"))
password = URL.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[2]/div/input")
password.send_keys("juan7890")#密碼

password.send_keys(Keys.ENTER)#打完帳密按下Enter

def three_times_add_member():
    time.sleep(5)
    wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div/button[2]"))
    add_member = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div/button[2]")
    add_member.click()#新增會員

def data_source():
    time.sleep(2)
    wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div/div/label[2]/span[1]"))
    manually_input = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div/div/label[2]/span[1]")
    manually_input.click()#手動輸入

#----新增會員----
three_times_add_member()
#----資料來源----
data_source()
#----會員資訊-----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[2]/div/div/div/input"))
input_OneClub_ID = URL.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[2]/div/div/div/input")
input_OneClub_ID.send_keys("green007")#輸入OneClub ID

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[3]/div/div/div/input"))
input_neme = URL.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[3]/div/div/div/input")
input_neme.send_keys("王測七")#輸入姓名

URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[6]/div/div/div/div/input"))
choose_counseling_teacher = URL.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[6]/div/div/div/div/input")
choose_counseling_teacher.send_keys("阮昱凱")
choose_counseling_teacher.send_keys(Keys.DOWN)
choose_counseling_teacher.send_keys(Keys.ENTER)

#---基本資料----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[2]/div/div[2]/div/input"))
input_phone_number = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[2]/div/div[2]/div/input")
input_phone_number.send_keys("0933232234")#輸入電話號碼

URL.execute_script("window.scrollBy(0,500)")


wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[3]/div/div/div/input"))
input_email = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[3]/div/div/div/input")
input_email.send_keys("juan123@gmail.com")#輸入電子郵件

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[2]/div[1]/div/div/input"))
choose_city = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[2]/div[1]/div/div/input")
choose_city.send_keys("新北市")#選擇縣市
choose_city.send_keys(Keys.DOWN)
choose_city.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[2]/div[2]/div/div/input"))
choose_district =URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[2]/div[2]/div/div/input")
choose_district.send_keys("板橋")#選擇區域
choose_district.send_keys(Keys.DOWN)
choose_district.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[3]/div/input"))
input_address = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[3]/div/input")
input_address.send_keys("中正路100號")#輸入地址

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[5]/div/div/label/span[1]/input"))
check_same_reach_out_address = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[5]/div/div/label/span[1]/input")
check_same_reach_out_address.click()#勾選同聯絡地址


wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[6]/button[2]"))
save = URL.find_element("xpath","/html/body/div/div[2]/main/div[6]/button[2]")
save.click()#儲存

#----建立學生----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/table/tbody/tr[1]/td[9]/button"))
edit = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/table/tbody/tr[1]/td[9]/button")
edit.click()#編輯

URL.switch_to.window(URL.window_handles[1])#切換到另一個分頁
time.sleep(5)
URL.execute_script("window.scrollBy(0,1000)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[1]/div/button"))
add_student = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[1]/div/button")
add_student.click()#新增學員

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div/div/input"))
input_studnet_name = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div/div/input")
input_studnet_name.send_keys("王學一")#輸入姓名

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div/div/div/input"))
input_educational_stage = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div/div/div/input")
input_educational_stage.send_keys("國小")#輸入學制
input_educational_stage.send_keys(Keys.DOWN)
input_educational_stage.send_keys(Keys.DOWN)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[2]/div/div/div/input"))
input_grade = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[2]/div/div/div/input")
input_grade.send_keys("一年級")#輸入年級
input_grade.send_keys(Keys.DOWN)
input_grade.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[1]/div/div/input"))
input_school_country = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[1]/div/div/input")
input_school_country.send_keys("新北市")#輸入學校縣市

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/div/input"))
input_school_district = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/div/input")
input_school_district.send_keys("板橋區")#輸入學校區域
input_school_district.send_keys(Keys.DOWN)
input_school_district.send_keys(Keys.ENTER)

URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[3]/div/div/input"))
input_school_name = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[3]/div/div/input")
input_school_name.send_keys("大觀國小")#輸入學校名稱
input_school_name.send_keys(Keys.DOWN)
input_school_name.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[1]/div/div/input"))
Shipping_address_Country = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[1]/div/div/input")
Shipping_address_Country.send_keys("新北市")#輸入寄送地址(縣市)
Shipping_address_Country.send_keys(Keys.DOWN)
Shipping_address_Country.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[2]/div/div/input"))
Shipping_address_district = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[2]/div/div/input")
Shipping_address_district.send_keys("板橋區")#輸入寄送地址(區域)
Shipping_address_district.send_keys(Keys.DOWN)
Shipping_address_district.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[3]/div/input"))
Shipping_address_address = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[3]/div/input")
Shipping_address_address.send_keys("中正路100號")#輸入寄送地址(地址)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[5]/button[2]"))
add_button = URL.find_element("xpath","/html/body/div/div[2]/main/div[5]/button[2]")
add_button.click()#新增

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/button"))
back_button = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/button")
back_button.click()#返回

#----切換到一般課程---








