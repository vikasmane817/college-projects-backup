import time
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\Vikas\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://in.mail.yahoo.com")
expectedTitle="Yahoo Mail"
homepagetitle=driver.title

if expectedTitle == homepagetitle:
    print("pass")
else:
    print("fail")


signin = driver.find_element_by_xpath('//*[@id="signin-main"]/div[1]/a')
signin.click()
expectedpage='https://in.mail.yahoo.com/'
loginpagetitle=driver.current_url

if expectedpage==loginpagetitle:
    print('pass')
else:
    print('fail')


time.sleep(5)
usernamebox=driver.find_element_by_xpath('//*[@id="login-username"]')
usernamebox.send_keys('vikasmane817@yahoo.com')


nextButton=driver.find_element_by_xpath('//*[@id="login-signin"]')
nextButton.click()
time.sleep(3)
passwordarea=driver.find_element_by_xpath('//*[@id="login-passwd"]')
passwordarea.send_keys('viki@123')
time.sleep(2)
nextButtonpsw=driver.find_element_by_xpath('//*[@id="login-signin"]')
nextButtonpsw.click()
time.sleep(2)
if driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/nav/div/div[3]/div[3]/ul/li[1]/div/a/span[1]/span/span/span')==driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/nav/div/div[3]/div[3]/ul/li[1]/div/a/span[1]/span/span/span'):
    print('pass')
else:
    print('fail')

userbutton=driver.find_element_by_xpath('//*[@id="ybarAccountMenuOpener"]')
userbutton.click()
time.sleep(1)
logoutbutton=driver.find_element_by_xpath('//*[@id="profile-signout-link"]')
logoutbutton.click()
time.sleep(2)
afterlogouturl='https://in.search.yahoo.com/?fr2=inr'
if afterlogouturl==driver.current_url:
    print('pass')
else:
    print('fail')

driver.quit()

###negative test 

driver=webdriver.Chrome(executable_path="C:\\Users\\Vikas\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://in.mail.yahoo.com")
expectedTitle="Yahoo Mail"
homepagetitle=driver.title

if expectedTitle == homepagetitle:
    print("pass")
else:
    print("fail")


signin = driver.find_element_by_xpath('//*[@id="signin-main"]/div[1]/a')
signin.click()
expectedpage='https://in.mail.yahoo.com/'
loginpagetitle=driver.current_url

if expectedpage==loginpagetitle:
    print('pass')
else:
    print('fail')


time.sleep(5)
usernamebox=driver.find_element_by_xpath('//*[@id="login-username"]')
usernamebox.send_keys('vikasmane817@yahoo.com')


nextButton=driver.find_element_by_xpath('//*[@id="login-signin"]')
nextButton.click()
time.sleep(3)
passwordarea=driver.find_element_by_xpath('//*[@id="login-passwd"]')
passwordarea.send_keys('viki123')
time.sleep(2)
nextButtonpsw=driver.find_element_by_xpath('//*[@id="login-signin"]')
nextButtonpsw.click()
time.sleep(2)
expectedurl='https://login.yahoo.com/account/challenge/password?pspid=1197806870&activity=header-signin&.lang=en-IN&.intl=in&src=ym&done=https%3A%2F%2Fin.mail.yahoo.com%2Fd&acrumb=u2fCHgz6&display=login&authMechanism=primary&sessionIndex=QQ--&e=true&pcn=password'
if expectedurl==driver.current_url:
    print('pass')
else:
    print('fail')


driver.quit()