import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By


class AutTest(unittest.TestCase):

    # Method ini dijalankan sebelum setiap test
    def setUp(self):
        # Konfigurasi Firefox
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        # Alamat Selenium Hub
        server = "http://localhost:4444"

        # Menghubungkan Selenium ke Firefox di container
        self.browser = webdriver.Remote(
            command_executor=server,
            options=options
        )

        # Menutup browser otomatis setelah test selesai
        self.addCleanup(self.browser.quit)

    # Test untuk halaman utama AUT
    def test_homepage(self):

        # Jika ada parameter URL dari command line, gunakan itu
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            # Default URL (AUT)
            url = "http://localhost"

        # Membuka halaman AUT
        self.browser.get(url)

        # Hasil yang diharapkan muncul di halaman
        expected_result = "Welcome back, Guest!"

        # Mengambil elemen <p> dari halaman
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')

        # Validasi apakah teks sesuai dengan yang diharapkan
        self.assertIn(expected_result, actual_result.text)


# Menjalankan test jika file dieksekusi langsung
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')
