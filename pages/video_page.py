from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class VideoPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_group = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2)")
        self.btn_lessons = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)")
        self.btn_look = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(4) > div.flex.gap20 > div:nth-child(8) > div.lesson-card > div > div.lesson-card-left > div.lesson-card-left_actions > button")
        # self.btn_fullscreen = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button.baseicon.baseavatar_fullscreen")
        self.btn_play = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")
        self.btn_grade = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div.videolesson__general-footer-rating.mb10 > div > div > div > span:nth-child(5)")
        # self.btn_choose = (By.CSS_SELECTOR, "#app > #dialog > div > div > div > div > div > div.flex.jcc.gap5")
        # self.btn_send = (By.CSS_SELECTOR, "#dialog > div > div > div > div > div > button")

    def click_btn_group(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_group)).click()

    def click_btn_lessons(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_lessons)).click()

    def click_btn_look(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_look)).click()

    def click_btn_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen)).click()

    def click_btn_play(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_play)).click()

    def click_btn_grade(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_grade)).click()

    # def click_btn_choose(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.btn_choose)).click()

    def click_btn_send(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_send)).click()




