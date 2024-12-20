from seleniumbase import Driver
from selenium.webdriver.common.by import By 
from selenium.webdriver import ActionChains 
from time import sleep 

driver = Driver (uc=True)

url = "https://democaptcha.com/demo-form-eng/hcaptcha.html" 
driver.get(url) 
sleep(2) 
iframe = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/iframe') 
driver.switch_to_frame(iframe)
input("start")
pos = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
def gridT(pos):
    
    boxes = driver.find_elements(By.XPATH,'/html/body/div/div[1]/div/div/div[2]/div')
    for boxe in range(9):
        if pos[boxe]:
           boxes[boxe].click()
    
    
gridT(pos)
input("end.")