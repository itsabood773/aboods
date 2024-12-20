from seleniumbase import Driver
from selenium.webdriver.common.by import By 
from selenium.webdriver import ActionChains 
from time import sleep 

driver = Driver (uc=True)

url = "https://democaptcha.com/demo-form-eng/hcaptcha.html" 
driver.get(url) 
sleep(2) 
iframe = driver.find_element(By.CSS_SELECTOR,'form  iframe') 
driver.switch_to_frame(iframe)
sleep(1)
posG = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
def gridT(pos):
    
    boxes = driver.find_elements(By.XPATH,'/html/body/div/div[1]/div/div/div[2]/div')
    for boxe in range(9):
        if pos[boxe]:
           boxes[boxe].click()
           
posC = [[10, 10], [20, 33]]
def canvaT(posC):
    space = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div/canvas')
    for pos_ in posC:
        x = pos_[0]
        y = pos_[1]
        actions = ActionChains(driver) 
        actions.move_to_element_with_offset(space, x, y)
        actions.click()
        actions.perform()


checkbox = driver.find_element(By.XPATH,'//*[@id="checkbox"]')
checkbox.click()

input("end")
driver.save_screenshot("main.png")