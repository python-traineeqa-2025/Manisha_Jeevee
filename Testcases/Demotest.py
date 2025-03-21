import time
import selenium
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.jeevee.com/')
create_account = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//div[contains(@class,\'user_greetings__29Sj5 md:block relative\')]//div[contains(@class,\'flex space-x-0.5 sm:space-x-1 lg:space-x-1.5 items-center cursor-pointer shrink\')]//*[name()=\'svg\']//*[name()=\'path\' and contains(@d,\'M47.76 482\')]'))
)

login = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[4]/div[1]/div[2]/div[2]/div[9]'))
)

actions = ActionChains(driver)
actions.move_to_element(create_account).move_to_element(login).click().perform()
time.sleep(2)
# except selenium.common.exceptions.TimeoutException:
#     print("Element not found within the given time frame")
# finally:
#     driver.quit()

mobile_number =  WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder=\'Mobile Number *\']'))
)
mobile_number.click()
mobile_number.send_keys("9745917977")

password = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,'input[placeholder=\'Password *\']'))
)
password.click()
password.send_keys("Nec@019326")

login_btn =  WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//button[normalize-space()=\'Sign In\']'))
)
login_btn.click()

time.sleep(10)

searchbar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[contains(@class,\'hidden sm:block grow mx-2.5 py-2.5 relative w-auto\')]//input[contains(@placeholder,\'Search for Products, Medicine...\')]'))
)
searchbar.click()
searchbar.send_keys("Sunscreen")
time.sleep(2)

# wait = WebDriverWait(driver, 10)

# Wait for all suggestion elements
list1 = driver.find_elements(By.XPATH,"//div[@class='pt-2']//span")

for item in list1:
    print(item.text)
    if item.text.strip() == "Ethisun sunscreen-100gm":
        item.click()
        break

time.sleep(5)

cart = driver.find_element(By.XPATH,'//button[normalize-space()=\'Add to Cart\']')
cart.click()
time.sleep(5)




