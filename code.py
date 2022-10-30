from selenium import webdriver  				# be sure to downloard selenium and have chromedriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver.exe")   # put the path of where your chromedriver is located
driver.get("https://tellonym.me/XXXX")     		# link the tellonym here
time.sleep(2)


while True:
    text = driver.find_element(By.NAME, 'tell')
    text.send_keys('Cachez vos femmes, vos sœurs, vos mères, vos tantes et tout ce qui possède une chatte, Armand Muslim est en ville.')  # put the the text you want to send in the ''

    time.sleep(5)

    send = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[2]/div[2]/div/div[2]/form/button')
    send.click()

    time.sleep(4)

    re = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[3]')
    re.click()
