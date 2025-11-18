import pytest
import time
from time import sleep
from selenium.common.exceptions import TimeoutException
from pages.auth_page import AuthPage
from pages.home_page import HomePage
# from pages.video_page import VideoPage
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


def test_auth_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_chrome)
    auth_page.input_login("998993202513")
    auth_page.click_btn_next()
    auth_page.input_password("timka131313")
    auth_page.click_btn_submit()
    time.sleep(5)
    try:
        auth_page.click_btn_sessions()
        time.sleep(3)
        auth_page.click_btn_finish()
        time.sleep(1)
    except:
        pass

    home_page = HomePage(driver_chrome)
    time.sleep(3)
    home_page.click_btn_homework()
    time.sleep(3)
    home_page.input_comment("Thank you")
    time.sleep(6)
    home_page.click_btn_send()
    time.sleep(3)


    # home_page.click_btn_profile()
    # time.sleep(1)
    # home_page.click_btn_exit()
    # time.sleep(1)
    # home_page.click_btn_confirmation()
    # time.sleep(1)


    # video_page = VideoPage(driver_chrome)
    # time.sleep(5)
    # video_page.click_btn_group()
    # time.sleep(5)
    # video_page.click_btn_lessons()
    # time.sleep(5)
    # video_page.click_btn_look()
    # time.sleep(1)
    # video_page.click_btn_fullscreen()
    # time.sleep(1)
    # video_page.click_btn_play()
    # time.sleep(1)


    # try:
    #     video_page.click_btn_grade()
    #     time.sleep(3)
    #     # video_page.click_btn_choose()
    #     # time.sleep(3)
    #     video_page.click_btn_send()
    #     time.sleep(3)
    # except:
    #     pass


# def test_auth_chrome(driver_firefox):
#     driver_firefox.get("https://my.proweb.uz/log-in?q=/home")
#     auth_page = AuthPage(driver_firefox)
#     auth_page.input_login("998993202513")
#     auth_page.click_btn_next()
#     time.sleep(2)
#     auth_page.input_password("timka131313")
#     auth_page.click_btn_submit()
#     try:
#         auth_page.click_btn_sessions()
#         time.sleep(2)
#         auth_page.click_btn_finish()
#     except:
#         pass



# def test_auth_chrome(driver_edge):
#     driver_edge.get("https://my.proweb.uz/log-in?q=/home")
#     auth_page = AuthPage(driver_edge)
#     auth_page.input_login("998993202513")
#     auth_page.click_btn_next()
#     time.sleep(2)
#     auth_page.input_password("timka131313")
#     auth_page.click_btn_submit()
#     try:
#         auth_page.click_btn_sessions()
#         time.sleep(2)
#         auth_page.click_btn_finish()
#     except:
#         pass






