from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("==no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = options
)

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.btn_homework = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-homework.home__education-homework-works > div.tab-content.home__homeworks-tabview > div > div.home__works > div > div > div:nth-child(2) > div.home__homework-container")
        self.comment = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > div > div > label > textarea")
        self.btn_send = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > button")


    def click_btn_homework(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_homework)).click()

    def input_comment(self, comment):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.comment)).send_keys(comment)

    def click_btn_send(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_send)).click()




#         self.btn_profile = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar > div")
#         self.btn_exit = (By.CSS_SELECTOR, "#app > div > div.inforation > div > div > div:nth-child(6)")
#         self.btn_confirmation = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")
#         self.btn_profile = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar > div")


#     def click_btn_profile(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.btn_profile)).click()

#     def click_btn_exit(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.btn_exit)).click()

#     def click_btn_confirmation(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.btn_confirmation)).click()
