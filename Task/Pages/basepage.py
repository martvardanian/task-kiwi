import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator))).click()
        time.sleep(1)

    def get_text(self, by_locator):
        time.sleep(1)
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator))).text
        return text

    def send_keys(self, by_locator, text):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator))).send_keys(text)