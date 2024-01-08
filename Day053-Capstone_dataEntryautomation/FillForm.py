from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
import time
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSd1HbFgGTHCXHFB_lj3WZW4ymN3QZ2CUBhgGfsmHee4W0sEew/viewform?usp=sf_link"

class FillForm:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)
    def fill_form(self,info_list):
        self.driver.get(form_url)
        
        time.sleep(3)
        
        for info in info_list:
                    input_field = self.driver.find_elements(By.CSS_SELECTOR, value=".Xb9hP input")
                    input_field[0].send_keys(info["address"])
                    input_field[1].send_keys(info["price"])
                    input_field[2].send_keys(info["link"])
                    time.sleep(1)
                    submit = self.driver.find_element(By.CSS_SELECTOR, value='div[role = "button"]')
                    submit.click()
                    time.sleep(2)

                    go_back = self.driver.find_element(By.CSS_SELECTOR, value=".c2gzEf a")
                    go_back.click()
              
        print("Completed Sending data")