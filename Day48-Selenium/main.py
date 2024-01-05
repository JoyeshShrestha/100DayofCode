from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

upcoming_dict = {}
wanted_list=[]

for i in range(1,5):
    upcoming = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]').text
    list_upcoming = upcoming.split("\n")
    upcoming_dict={
        "time":list_upcoming[0],
        "Title":list_upcoming[1]
    }
    wanted_list.append(upcoming_dict)
print(wanted_list)



print(upcoming_dict)    
driver.quit()
