from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv
load_dotenv()




class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)
        
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        url="https://www.speedtest.net"
        self.driver.get(url)
        time.sleep(8)
        go = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go.click()
        time.sleep(60)
        loop = True
        while loop:
            time.sleep(10)

            try:
                close = self.driver.find_element(By.CSS_SELECTOR, value="button[class='close-btn pure-button pure-button-primary']")
                close.click()
            except(NoSuchElementException):
                print("not yet")    
            else:
                loop=False

            self.up = self.driver.find_element(By.CSS_SELECTOR,value=".upload-speed").text
            self.down = self.driver.find_element(By.CSS_SELECTOR,value=".download-speed").text
            print(f"upload:{self.up}------down:{self.down}")    
    def tweet_at_provider(self,p_up,p_down): 
        url = "https://twitter.com/home"
        self.driver.get(url)   
        time.sleep(7)
        print("ok")
        email = self.driver.find_element(By.CSS_SELECTOR,value='input[autocomplete = "username"]')
        email.click()
        email.send_keys(os.environ["Twiter_email"])
        time.sleep(2)
        email.send_keys(Keys.ENTER)
        time.sleep(5)

        second_page = self.driver.find_element(By.CSS_SELECTOR,value='input[name="text"]')
        second_page.click()
        second_page.send_keys("9843375283")
        time.sleep(2)
        second_page.send_keys(Keys.ENTER)
        time.sleep(3)


        password = self.driver.find_element(By.CSS_SELECTOR,value="input[autocomplete='current-password']")
        password.click()
        password.send_keys(os.environ["Linkedin_password"])
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        whats_happening = self.driver.find_element(By.CSS_SELECTOR,value="#react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > header > div > div > div > div:nth-child(1) > div.css-175oi2r.r-1p6iasa.r-e7q0ms.r-1awozwy > a")
        whats_happening.click()
        time.sleep(5)


        typeHere = self.driver.find_element(By.CSS_SELECTOR,value="div.DraftEditor-editorContainer > div > div > div > div > span")
        typeHere.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}/up when I pay for {p_down}down/{p_up}/up")
