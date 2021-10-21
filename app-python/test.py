import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class AllTests(unittest.TestCase):
    def setUp(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.options)

    def test_user_can_loging(self):
        self.driver.get("http://localhost/login")
        self.driver.find_element_by_name("username").send_keys("asdadmin")
        self.driver.find_element_by_name("password").send_keys("admasdin")
        self.driver.find_element_by_name("login").click()
        print(self.driver.current_url)
        self.assertIn('http://localhost/login-ok', self.driver.current_url)
        assert "No results found." not in self.driver.page_source

if __name__ == "__main__":
    unittest.main()
