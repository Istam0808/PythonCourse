# import time
# import unittest

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# # https://chromedriver.chromium.org/downloads
# PATH = "D:\\Pythonres\\chromedriver.exe"

# HALF_SECOND = 0.5


# class Fullstack(unittest.TestCase):

#     def setUp(self):
#         options = Options()
#         # options.add_argument('--headless')
#         self.driver = webdriver.Chrome(service=Service(PATH), options=options)
#         self.driver.maximize_window()
#         # self.current_test = self.id().split(".")[-1]

#     def tearDown(self):
#         self.driver.close()
#         self.driver.quit()
#         print(f"Ending test for {self.driver}")

#     def test_login_to_facebook(self):
#         pass

#     def test_wikipedia(self):
#         self.driver.get("https://www.wikipedia.org/")
#         print("Getting url...")
#         slogan = self.driver.find_element(By.CLASS_NAME, "localized-slogan")
#         print(slogan)
#         print("ID: -> ", slogan.get_property("id"))
#         print("link.text: -> ", slogan.text)

#         text_to_write = "FullStack programming"
#         search_input = self.driver.find_element(By.ID, "searchInput")
#         search_input.send_keys(text_to_write)
#         time.sleep(HALF_SECOND)
#         btn = self.driver.find_element(By.CLASS_NAME, "svg-search-icon")
#         btn.click()
#         time.sleep(HALF_SECOND*2)
#         expected_heading = self.driver.find_element(By.ID, "firstHeading")
#         assert expected_heading.text == "Search results"
#         assert "Search results" in self.driver.page_source

















# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url="https://www.instagram.com/"

# def main():
#     def get_password():
#         return 'Xusen_553'#'Istamake_553'
    
    
#     driver=webdriver.Chrome()
#     driver.get(url=url)
#     sleep(2)
   
#     email='husen_ake07'
#     email_getter=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
#     email_getter.send_keys(email)
#     sleep(2)
    
#     pw_getter=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
#     pw_getter.send_keys(get_password())
   
#     btn=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
#     btn.click()
#     sleep(40)
    
# if __name__ == '__main__':
#     main()  




import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class InstagramRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.instagram.com/"
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        self.driver.get(url=self.url)
        sleep(2)

       
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        signup_link.click()
        sleep(2)


        email = 'husen_ake07'
        email_getter = self.driver.find_element(By.NAME, 'emailOrPhone')
        email_getter.send_keys(email)
        sleep(2)

        full_name = 'Husen Ake'
        full_name_getter = self.driver.find_element(By.NAME, 'fullName')
        full_name_getter.send_keys(full_name)
        sleep(2)

        password = 'Xusen_553'
        password_getter = self.driver.find_element(By.NAME, 'password')
        password_getter.send_keys(password)
        sleep(2)

        signup_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')
        signup_btn.click()
        sleep(5)

        profile_picture = self.driver.find_elements(By.CLASS_NAME, '_6q-tv')
        self.assertTrue(profile_picture, "Registration failed.")

if __name__ == '__main__':
    unittest.main()





















# from typing import Union, assert_never

# def handle_value(value: Union[int, str, float]):
#     if isinstance(value, int):
#         print("Handling an integer...")
#     elif isinstance(value, str):
#         print("Handling a string...")
#     elif isinstance(value, float):
#         print("Handling a float...")
#     else:
#         assert_never(value)

# handle_value([])


# import unittest

# class MyTest(unittest.TestCase):

#     def setUp(self):
#         self.var = 1

#     def tearDown(self):
#         self.var = None


#     def test(self):
#         self.assertEqual(1,1)

#     def test_2(self):
#         self.assertNotEqual(1,2)

#     def test_3(self):
#         self.assertTrue(True)

#     def test_4(self):
#         self.assertFalse(False)

#     def test_5(self):
#         self.assertIs(1,1)

#     def test_6(self):
#         self.assertIsNone(None)

#     def test_7(self):
#         self.assertIn(1, [1,2,3])

#     def test_8(self):
#         self.assertIsInstance(1,int)

# to run this test from command line:
# python -m unittest -v file_name.py
# -v  =>  verbose mode  (means that we will see all the output from the test)
# -m  =>  module  (means that we will run the test from the module)


# assertNotEqual(a, b): This assertion checks if a is not equal to b.

# assertTrue(x): This assertion checks if the value of x is True.

# assertFalse(x): This assertion checks if the value of x is False.

# assertIs(a, b): This assertion checks if a is b.

# assertIsNone(x): This assertion checks if the value of x is None.

# assertIn(a, b): This assertion checks if a is in b.

# assertIsInstance(a, b): This assertion checks if a is an instance of b.
