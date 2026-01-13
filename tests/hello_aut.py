import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        server = "http://localhost:4444"

        self.browser = webdriver.Remote(
            command_executor=server,
            options=options
        )

        self.addCleanup(self.browser.quit)

    def test_homepage(self):

        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            # akses AUT via docker network
            url = "http://docker-apache"

        self.browser.get(url)

        expected_result = "Welcome back, Guest!"

        wait = WebDriverWait(self.browser, 15)
        element = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )

        self.assertIn(expected_result, element.text)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')
