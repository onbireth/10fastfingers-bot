from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(options=chrome_options)

def login():
    driver.get("https://10fastfingers.com/login")
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
    
    inputt = driver.find_element(By.XPATH,"//*[@id='UserEmail']")
    inputt.send_keys("Your email address")
    
    inputt2 = driver.find_element(By.XPATH,"//*[@id='UserPassword']")
    inputt2.send_keys("Your password")
    driver.find_element(By.XPATH,"//*[@id='login-form-submit']").click()

login()
driver.implicitly_wait(5)
count = 1
while True:
    input = driver.find_element(By.ID,"inputfield")
    span=driver.find_element(By.XPATH,f"//*[@id='row1']/span[{count}]")
    text = a.text
    input.send_keys(text, Keys.SPACE)
    count +=1
    if count == 400:
        break

