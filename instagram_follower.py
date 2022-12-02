from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time


options = Options()
options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()), options=options
        )
        self.modal = None

    def login(self, user, passw):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        password = self.driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        username.send_keys(user)
        password.send_keys(passw)
        password.send_keys(Keys.ENTER)

    def follow(self, sim_account):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{sim_account}/")

        time.sleep(5)
        followers = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div',
        )
        time.sleep(5)
        followers.click()

        time.sleep(5)

        modal = self.driver.find_element(
            By.XPATH, "/html/body/div[6]/div/div/div/div[2]/ul/div"
        )
        for i in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal
            )
            time.sleep(2)

        time.sleep(2)
        buttons = modal.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(
                    By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]"
                )
                cancel_button.click()
