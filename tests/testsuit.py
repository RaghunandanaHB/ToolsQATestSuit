import time

from selenium.webdriver.support.select import Select

from pageObjects.demoSite import demoSite
from pageObjects.homePage import homePage
from pageObjects.seleniumTraining import seliniumTraining
from pageObjects.youTube import youTube
from utilities.baseclass import baseClass


class Test_suit(baseClass):

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
        self.driver.close()

        # # Switching back to parent window
        self.driver.switch_to.window(self.driver.window_handles[0])

        homepage.youtubeChannelLink().click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        text2 = youtube.channelName().text
        assert text1 == text2
        print("The channel navigated via Youtube Link is " + text2)


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



    def test_TQA003(self):
        homepage = homePage(self.driver)
        homepage.demoSite().click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        demosite = demoSite(self.driver)
        self.driver.execute_script("window.scrollTo(0,500)")
        demosite.Elements().click()
        demosite.radioButton().click()
        demosite.impressiveButton().click()
        msg = demosite.confirmationMgs().text
        assert "Impressive" == msg
        print("The selected radio button is "+msg)


# TQA004 : Open website > Tap on demo site > Tap on web tables > Delete the entries if any > Add a new entry
#          > make sure it is displayed under the table

    def test_TQA004(self):
        homepage = homePage(self.driver)
        homepage.demoSite().click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        demosite = demoSite(self.driver)
        self.driver.execute_script("window.scrollTo(0,500)")
        demosite.Elements().click()
        demosite.webTables().click()

        # Deleting the entries
        a = demosite.deleteButton()
        # counting th number of entries through Delete Button
        for i in a:b
            n=0
            n=n+1
            demosite.deleteButton().click()
            time.sleep(3)
            print(n)







        time.sleep(2)
