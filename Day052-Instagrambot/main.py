from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
import time
import os
from dotenv import load_dotenv
load_dotenv()
TO_FOLLOW = "amtakethat"

class InstagramBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com"
        self.driver.get(url)
        time.sleep(3)
        username = self.driver.find_element(By.CSS_SELECTOR,"input[name='username']")
        username.click()
        username.send_keys(os.environ["INSTA_USERNAME"])
        password = self.driver.find_element(By.CSS_SELECTOR,value="input[name='password']")
        password.click()
        password.send_keys(os.environ["Linkedin_password"])
        login = self.driver.find_element(By.CSS_SELECTOR,value="button[type='submit']")
        login.click()

    def search(self):
        time.sleep(10)
        try:
    
            search_button = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a')
            search_button.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

        time.sleep(2)
        search_input = self.driver.find_element(By.CSS_SELECTOR,value="input[aria-label='Search input']")
        search_input.click()
        search_input.send_keys(TO_FOLLOW)
        time.sleep(2)
        to_follow_button = self.driver.find_element(By.CSS_SELECTOR,value="div div[role='none'] a")
        to_follow_button.click()
        time.sleep(5)
        click_followers = self.driver.find_element(By.CSS_SELECTOR,value= 'ul li:nth-child(2) a')
        click_followers.click()
        time.sleep(2)
        follower_list = self.driver.find_elements(By.CSS_SELECTOR,value="._aano button")
        time.sleep(2)
        print(follower_list)
        print(len(follower_list))

        
        for follower in follower_list:
            time.sleep(3)
            print("start ")
            try:                
                follower.click()
            except(ElementClickInterceptedException):
                        cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                        cancel_button.click()
            
            

            

            
instagram = InstagramBot()
instagram.login()
instagram.search()