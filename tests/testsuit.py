import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from pageObjects.demoSite import demoSite
from pageObjects.homePage import homePage
from pageObjects.qa_practices import qa_tutorials
from pageObjects.seleniumTraining import seliniumTraining
from pageObjects.youTube import youTube
from utilities.baseclass import baseClass


class Test_suit(baseClass):


 # # TQA001 : Open website > In YouTube section tap on subscribe >Tap on youtube Channel link > New window openes
 # #          > Check both the links navigate to the same channel

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

# # TQA002 : Open website > Tap on Selenium training tab > Tap on Go to regestration button > Enter required fields
# #          > Confirmation message should be displayed

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


# # TQA003 : Open website > Tap on demo site > Tap on elements > tap on radio button > tap on any of the button
# #           > extract the text of confirmation message

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


# # TQA004 : Open website > Tap on demo site > Tap on web tables > Add a new entry > assert to confirm it is displayed in the table

    def test_TQA004(self):
        homepage = homePage(self.driver)
        homepage.demoSite().click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        demosite = demoSite(self.driver)
        self.driver.execute_script("window.scrollTo(0,500)")
        demosite.Elements().click()
        demosite.webTables().click()
        demosite.Addbutton().click()
        demosite.firstName().send_keys("Jaggesh")
        demosite.lastName().send_keys("upendra")
        demosite.Email().send_keys("jaggesh@jademaysandra.com")
        demosite.Age().send_keys("22")
        demosite.Salary().send_keys("120000")
        demosite.Department().send_keys("Civil")
        demosite.Submitbutton().click()
        first_name_enterd = demosite.Firstnameconfirm().text
        assert "Jaggesh" == first_name_enterd
        print("All the entries are registered")


# # TQA005 :  Open website > Tap on tutorials >  QA Practices > Software Testing > Display the content which is under the 'Ways of testing'

    def test_TQA005(self):
        homepage = homePage(self.driver)
        homepage.Tutorials().click()

        # mouse hover action
        mouse_hover = ActionChains(self.driver)
        mouse_hover.move_to_element(homepage.QA_practices()).perform()
        homepage.Software_testing().click()

        qatutorials = qa_tutorials(self.driver)
        software = qatutorials.Software_contents().text
        print(software)
        manual = qatutorials.Manual_contents().text
        print(manual)
        automation = qatutorials.Automation_contents().text
        print(automation)
