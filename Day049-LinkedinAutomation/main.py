from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
import os
from dotenv import load_dotenv
load_dotenv()



def abort():
    try:
        close = driver.find_element(By.CSS_SELECTOR,".artdeco-modal__dismiss")
        close.click()
        time.sleep(2)

        discard = driver.find_element(By.CSS_SELECTOR,value=".artdeco-modal__confirm-dialog-btn")
        discard.click()
    except(NoSuchElementException):
        pass    
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

Linkedin_url="https://www.linkedin.com/jobs/search/?currentJobId=3784589880&f_AL=true&f_WT=2&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
driver.get(Linkedin_url)
loop = True
while loop:
    try:
        sign_in = driver.find_element(By.CSS_SELECTOR,value="body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis")

        sign_in.click()
    except(NoSuchElementException):
        continue
    else:
        loop=False    
time.sleep(5)


user_name = driver.find_element(By.ID,value="username")
user_name.send_keys("sjoyesh2000@gmail.com")
password = driver.find_element(By.ID,value="password")
password.send_keys(os.environ["Linkedin_password"])

submit_button = driver.find_element(By.CSS_SELECTOR,value=".login__form_action_container button")
submit_button.click()

time.sleep(2)
list_jobs = driver.find_elements(By.CLASS_NAME, value="scaffold-layout__list-container li div div")

print(list_jobs)
for job in list_jobs:
    print("Opening Listing")
    job.click()
    time.sleep(7)
    try:

        easy_apply = driver.find_element(By.CLASS_NAME,value="jobs-apply-button")
        easy_apply.click()
        time.sleep(2)

        # phone_number = driver.find_element(By.CSS_SELECTOR, value="#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3732528413-9-phoneNumber-nationalNumber")
        
        # if phone_number.text == "":
        #     phone_number.send_keys(os.environ["Phone_number"])
        time.sleep(2)
        
        submit_app_button = driver.find_element(By.CSS_SELECTOR,value="button[aria-label='Submit application']")
        print("BUTONNN",submit_app_button.text)
        submit_app_button.click()
        time.sleep(2)
        done = driver.find_element(By.CSS_SELECTOR, value="button[aria-label='Dismiss']")
        done.click()

        print("Submitting job application")
    except (NoSuchElementException):
        abort()
        print("nope")
        pass


    # next_1 = driver.find_element(By.CSS_SELECTOR,value="#ember440")
    # next_1.click()




