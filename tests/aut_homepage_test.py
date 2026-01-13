import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutHomepageTest(unittest.TestCase):

    def setUp(self):
        # Ambil nama browser dari argumen (firefox / chrome / edge)
        self.browser_name = sys.argv[1] if len(sys.argv) > 1 else "firefox"

        if self.browser_name == "chrome":
            options = webdriver.ChromeOptions()
        elif self.browser_name == "edge":
            options = webdriver.EdgeOptions()
        else:
            options = webdriver.FirefoxOptions()

        # Hub Selenium
        server = "http://localhost:4444"

        self.browser = webdriver.Remote(
            command_executor=server,
            options=options
        )

        self.wait = WebDriverWait(self.browser, 20)
        self.addCleanup(self.browser.quit)

    def test_aut_homepage(self):
        # Ambil URL AUT dari argumen
        url = sys.argv[2] if len(sys.argv) > 2 else "http://localhost"

        self.browser.get(url)

        # Tunggu sampai <h1> muncul
        h1 = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        # Simpan screenshot
        screenshot_name = f"aut_{self.browser_name}.png"
        self.browser.save_screenshot(screenshot_name)

        # Validasi teks halaman
        self.assertIn("AUT is running successfully", h1.text)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2)
