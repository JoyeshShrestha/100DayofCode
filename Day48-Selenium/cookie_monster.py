from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")



def click_cookie():
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()

def check_options():
    points = driver.find_element(By.ID, value="money").text
    right_panel = driver.find_elements(By.CSS_SELECTOR, value = "#rightPanel #store div b")
    grayed =  driver.find_elements(By.CSS_SELECTOR, value = "#rightPanel #store .grayed b")
    
    # price = [prices.text.split()[-1] for prices in right_panel]
    available_panel=[]
    # print(grayed)
    for panel in right_panel:
        if panel not in grayed:
            available_panel.append(panel.text)

    # available_panel = [available.text for available in right_panel if available not in grayed]
    prices = [p.split()[-1] for p in available_panel]
    which_can_be_bought = [p for p in prices if int(p) <= int(points)]
    maximum = which_can_be_bought[-1]
    index_of_maximum = prices.index(maximum)

    right_panel[index_of_maximum].click()
    print(prices)
    # for r in available_panel:
    #     price_element = r.text
    #     price = price_element.split()
    #     try:
    #         prices.append(price[-1])
    #     except(IndexError):
    #         pass    
    # return prices,points
    
loop=True
end = time.time() + 60*1
timeout = time.time() + 8
while loop:
    click_cookie()
    if time.time() > timeout:
        check_options()
        
        timeout = time.time() + 8
    if time.time() > end:
        loop=False
points = driver.find_element(By.ID, value="cps").text

print("Your final clicks per second is ",points.split()[-1])        
