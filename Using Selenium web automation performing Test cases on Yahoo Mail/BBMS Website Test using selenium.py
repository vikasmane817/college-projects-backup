from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\\Users\\Vikas\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()


driver.get("http://localhost/bbdms/admin/")
time.sleep(2)

test0='http://localhost/bbdms/admin/'

if(test0==driver.current_url):
    print("pass")
else:
    print("fail")

username=driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/form/input[1]')
username.send_keys('admin')

password=driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/form/input[2]')
password.send_keys('Test@12345')

loginButton=driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/form/button')
loginButton.click()
time.sleep(2)

test1='http://localhost/bbdms/admin/change-password.php'
if(test1==driver.current_url):
    print("pass")
else:
    print("fail")

dashboard=driver.find_element_by_xpath('/html/body/div[2]/nav/ul/li[2]/a')
dashboard.click()
test5='http://localhost/bbdms/admin/dashboard.php'
if(test5==driver.current_url):
    print("pass")
else:
    print('fail')
time.sleep(2)

blooddonor=driver.find_element_by_xpath('/html/body/div[2]/nav/ul/li[4]/a')
blooddonor.click()
test6='http://localhost/bbdms/admin/add-donor.php'
if(test6==driver.current_url):
    print('pass')
else:
    print('fail')
time.sleep(2)

donorlist=driver.find_element_by_xpath('/html/body/div[2]/nav/ul/li[5]/a')
donorlist.click()
test7='http://localhost/bbdms/admin/donor-list.php'
if(test7==driver.current_url):
    print('pass')
else:
    print('fail')
time.sleep(2)

tempbt=driver.find_element_by_xpath('/html/body/div[1]/ul/li/a')
tempbt.click()
logoutbt=driver.find_element_by_xpath('/html/body/div[1]/ul/li/ul/li[2]/a')
logoutbt.click()

test2='http://localhost/bbdms/admin/index.php'
if(test2==driver.current_url):
    print("pass")
else:
    print("fail")
time.sleep(2)

driver.quit()

