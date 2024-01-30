from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
import page

cs = Service('chromedriver.exe')
co = webdriver.ChromeOptions()

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        print('setup')
        self.driver = webdriver.Chrome(service=cs, options=co)
        self.driver.get('https://www.python.org/')
        print("setUp") 

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
    