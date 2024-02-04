from selenium.webdriver.common.by import By


class homePage:

    def __init__(self, driver):
        self.driver = driver

    subscribebutton = By.XPATH, "//a[text()='+ Subscribe']"

    acceptbutton = By.ID, "accept-cookie-policy"

    youtubechannellink = By.XPATH, "//a[text()='Youtube Channel']"

    seleniumbutton = By.XPATH, "(//a[text()='Selenium Training'])[1]"

    def subscribeButton(self):
        return self.driver.find_element(*homePage.subscribebutton)

    def acceptButton(self):
        return self.driver.find_element(*homePage.acceptbutton)

    def youtubeChannelLink(self):
        return self.driver.find_element(*homePage.youtubechannellink)

    def seleniumButton(self):
        return self.driver.find_element(*homePage.seleniumbutton)
