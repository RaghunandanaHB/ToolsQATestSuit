import time

from selenium.webdriver.support.select import Select

from pageObjects.homePage import homePage
from pageObjects.seleniumTraining import seliniumTraining
from pageObjects.youTube import youTube
from utilities.baseclass import baseClass


class Test_suit(baseClass):

    # # TQA001 : Open website > In Youtube section tap on subscribe >Tap on youtube Channel link
    # #  > New window openes > Check both the links navigate to the same channel
    def test_TQA001(self):
        homepage = homePage(self.driver)

        # # To accept the cookies
        homepage.acceptButton().click()

        homepage.subscribeButton().click()

        # # Switching to new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        youtube = youTube(self.driver)
        text1 = youtube.channelName().text
        print("The Channel navigated via subscribe button is " + text1)

        # # Switching back to parent window
        self.driver.switch_to.window(self.driver.window_handles[0])

        homepage.youtubeChannelLink().click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        text2 = youtube.channelName().text
        assert text1 == text2
        print("The channel navigated via Youtube Link is " + text2)


    # # TQA002 : Open website > Tap on Selenium training tab >
    # # Tap on Go to regestration button > Enter required fields > Confirmation message should be displayed
    def test_TQA002(self):
        homepage = homePage(self.driver)
        homepage.seleniumButton().click()

        seleniumtraining = seliniumTraining(self.driver)
        seleniumtraining.go_to_Registration().click()
        seleniumtraining.firstName().send_keys("Jack")
        seleniumtraining.lastName().send_keys("Sparrow")
        seleniumtraining.eMail().send_keys("pirates_of_the_caribbean@gmail.com")
        seleniumtraining.mobile_Number().send_keys("007003002123")

        # # Static drop down
        drop = Select(seleniumtraining.dropDown())
        drop.select_by_visible_text("India")

        seleniumtraining.cityName().send_keys("Beachfront")
        seleniumtraining.messAge().send_keys("Hi this is my first Automation script")
        seleniumtraining.code_Msg().send_keys("code")
        seleniumtraining.submit_Button().click()
        toast = seleniumtraining.error_Msg().text
        print(toast)
        assert "Unable" in toast