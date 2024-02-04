from selenium.webdriver.common.by import By


class seliniumTraining:

    def __init__(self, driver):
        self.driver = driver

    go_to_registration = By.XPATH, "(//a[@href='#enroll-form'])[1]"

    firstname = By.ID, "first-name"

    lastname = By.ID, "last-name"

    email = By.ID, "email"

    mobile_number = By.ID, "mobile"

    dropdown = By.ID, "country"

    cityname = By.ID, "city"

    message = By.ID, "message"

    code_msg = By.ID, "code"

    submit_button = By.XPATH, "//button[@class='btn btn-block btn-primary']"

    error_msg = By.XPATH, "//div[@class='alert alert-error']"

    def go_to_Registration(self):
        return self.driver.find_element(*seliniumTraining.go_to_registration)
    def firstName(self):
        return self.driver.find_element(*seliniumTraining.firstname)

    def lastName(self):
        return self.driver.find_element(*seliniumTraining.lastname)

    def eMail(self):
        return self.driver.find_element(*seliniumTraining.email)

    def mobile_Number(self):
        return self.driver.find_element(*seliniumTraining.mobile_number)

    def dropDown(self):
        return self.driver.find_element(*seliniumTraining.dropdown)

    def cityName(self):
        return self.driver.find_element(*seliniumTraining.cityname)

    def messAge(self):
        return self.driver.find_element(*seliniumTraining.message)

    def code_Msg(self):
        return self.driver.find_element(*seliniumTraining.code_msg)

    def submit_Button(self):
        return self.driver.find_element(*seliniumTraining.submit_button)

    def error_Msg(self):
        return self.driver.find_element(*seliniumTraining.error_msg)