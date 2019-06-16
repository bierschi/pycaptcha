from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time


class Browser:

    def __init__(self, name='firefox', headless=True):
        """

        :param name:
        :param headless:

        my_proxy = "195.69.221.198:38701"
        self.proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': my_proxy,
            'ftpProxy': my_proxy,
            'sslProxy': my_proxy,
            'noProxy': ''
        })
        """
        prof = webdriver.FirefoxProfile()
        prof.set_preference("network.proxy.type", 1)
        prof.set_preference("network.proxy.http", "104.238.174.22")
        prof.set_preference("network.proxy.http_port", 3128)
        prof.set_preference("network.proxy.https", "104.238.174.22")
        prof.set_preference("network.proxy.https_port", 3128)
        prof.set_preference("network.proxy.ssl", "104.238.174.22")
        prof.set_preference("network.proxy.ssl_port", 3128)
        prof.set_preference("browser.privatebrowsing.autostart", True)
        prof.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")
        prof.update_preferences()

        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("'name' must be type of string")

        if self.name == 'firefox':
            if headless:
                self.options = FirefoxOptions().add_argument("--headless")
                self.browser = webdriver.Firefox(options=self.options, proxy=self.proxy)
            else:
                self.browser = webdriver.Firefox(firefox_profile=prof)

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
        username_field = self.browser.find_element_by_id("regUsername")
        username_field.send_keys('JKlllm')

        password_field = self.browser.find_element_by_id("regPassword").send_keys('test1234')

        self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))
        self.browser.delete_all_cookies()

        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "recaptcha-anchor")))
        ele = self.browser.find_element(By.ID, "recaptcha-anchor")
        # ActionChains(driver).move_to_element(ele).perform()
        ele.click()

    def find_recaptcha_audio(self, url):

        self.browser.get(url=url)

        self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))
        self.browser.delete_all_cookies()

        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "recaptcha-anchor")))
        ele = self.browser.find_element(By.ID, "recaptcha-anchor")
        # ActionChains(driver).move_to_element(ele).perform()
        ele.click()
        self.browser.switch_to_default_content()

        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title=\"recaptcha challenge\"]")))
        iframe = self.browser.find_element(By.CSS_SELECTOR, "iframe[title=\"recaptcha challenge\"]")
        self.browser.switch_to.frame(iframe)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.ID, "rc-imageselect")))
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.ID, "recaptcha-audio-button")))
        time.sleep(5)
        self.browser.find_element(By.ID, "recaptcha-audio-button").click()

if __name__ == '__main__':
    browser = Browser(headless=False)
    #browser.open(url="https://www.wieistmeineip.ch/")
    #browser.open("http://reddit.com")
    #browser.reddit()
    browser.find_recaptcha_audio(url="https://www.google.com/recaptcha/api2/demo")