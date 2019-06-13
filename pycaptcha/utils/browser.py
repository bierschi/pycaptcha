from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Browser:

    def __init__(self, name='firefox', headless=True):

        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("'name' must be type of string")

        if self.name == 'firefox':
            if headless:
                self.options = FirefoxOptions().add_argument("--headless")
                self.browser = webdriver.Firefox(options=self.options)
            else:
                self.browser = webdriver.Firefox()

        elif self.name == 'chrome':
            if headless:
                self.options = ChromeOptions().add_argument("--headless")
                self.browser = webdriver.Chrome(options=self.options)
            else:
                self.browser = webdriver.Chrome()

    def open(self, url):
        """

        :return:
        """

        self.browser.get(url=url)
        #self.browser.find_element(By.XPATH, "//*[@id=\"header-bottom-right\"]/span[1]/a").click()
        print(self.browser.find_element_by_xpath("//a[contains(@href, 'https://www.reddit.com/register/')]").click())
        self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))
        WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"regEmail\"]/div[6]/div/div/div/iframe")))
        email_field = self.browser.find_element(By.XPATH, "//*[@id=\"regEmail\"]/div[6]/div/div/div/iframe")
        email_field.send_keys('test@example.de')

    def delete_all_cookies(self):
        """

        :return:
        """
        self.browser.delete_all_cookies()

    def reddit(self):

        self.browser.get("https://www.reddit.com/register/?dest=https%3A%2F%2Fwww.reddit.com%2F")
        email_field = self.browser.find_element_by_id("regEmail")
        email_field.send_keys('test@example.de')
        self.browser.find_element_by_class_name("AnimatedForm__nextButton").click()
        email_field = self.browser.find_element_by_id("regUsername")
        email_field.send_keys('test@example.de')

if __name__ == '__main__':
    browser = Browser(headless=False)
    #browser.open("http://reddit.com")
    browser.reddit()