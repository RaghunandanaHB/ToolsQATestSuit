from selenium.webdriver.common.by import By


class youTube:

    def __init__(self, driver):
        self.driver = driver

    channelname = By.XPATH, "(//yt-formatted-string[text()='@toolsqa-destinationforqapr8414'])[2]"

    def channelName(self):
        return self.driver.find_element(*youTube.channelname)