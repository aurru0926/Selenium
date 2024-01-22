import unittest
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        
        
    def search_query(self, query):
        with webdriver.Firefox() as driver:
            driver.get("http://google.com")
            mainPage = page.MainPage(driver)
            assert mainPage.is_title_matches()
            mainPage.search_text_element = query
            mainPage.click_go_button()
            driver.save_screenshot(f'screenshot_{query}.png')
            search_result_page = page.SearchResultPage(driver)
            assert search_result_page.is_results_found()

    def test_search_python_concurrent(self):
        # List of search queries you want to scrape
        search_queries = ["How many calories in a banana", "How much HP does a 2022 Subaru wrx have?", "selenium"]

        
        max_threads = 3

       
        with ThreadPoolExecutor(max_threads) as executor:
            executor.map(self.search_query, search_queries)
            
    def tearDown(self):
        print("Finished")


if __name__ == "__main__":
    unittest.main()
