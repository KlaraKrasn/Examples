import time
from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import HtmlTestRunner
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")
        print("Wikipedia Url has ", requests.get("https://www.wikipedia.org").status_code, " as status Code")
        code = requests.get("https://www.wikipedia.org").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")

        if not "Wikipedia" in driver.title:
            raise Exception("Wikipedia page has wrong Title!")

        try:
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "searchInput")))

        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file("wiki_page_loading_error.png")
            driver.save_screenshot('wiki_page_loading_error.png')

        self.assertIn("Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem2 = driver.find_element(By.ID, "searchInput")
        elem2.send_keys("Earth")
        driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()

        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))

        self.assertIn("Earth - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")
        if not "Earth" in driver.title:
            raise Exception("Wikipedia Earth page Title is wrong!")
        time.sleep(2)

        driver.find_element(By.XPATH, "//span[@class='toctext'][contains(.,'Chronology')]").click()
        self.assertIn("Earth#Chronology", driver.current_url)
        print("Get Chronology")
        if not "Earth#Chronology" in driver.current_url:
            raise Exception("Didn't get Chronology")

        driver.find_element(By.XPATH, "//span[@class='toctext'][contains(.,'Hydrosphere')]").click()
        self.assertIn("Earth#Hydrosphere", driver.current_url)
        print("Get Hydrosphere")
        if not "Earth#Hydrosphere" in driver.current_url:
            raise Exception("Didn't get Hydrosphere")

        driver.find_element(By.XPATH, "//img[@src='//upload.wikimedia.org/wikipedia/commons/thumb/9/97"
                                      "/The_Earth_seen_from_Apollo_17.jpg/220px-The_Earth_seen_from_Apollo_17.jpg']").click()

        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@title,'Show next image')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@title,'Show next image')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='mw-mmv-close']").click()

        driver.find_element(By.XPATH, "//a[@href='#cite_note-SIMEK179-31'][contains(.,'[26]')]").click()

        self.assertIn("Earth#cite_note-SIMEK179-31", driver.current_url)
        print("get footnote")
        if not "Earth#cite_note-SIMEK179-31" in driver.current_url:
            raise Exception("Didn't get footnote")

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")
        print("Wikipedia Url has ", requests.get("https://www.wikipedia.org").status_code, " as status Code")
        code = requests.get("https://www.wikipedia.org").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")

        time.sleep(1)
        if not "Wikipedia" in driver.title:
            raise Exception("Wikipedia page has wrong Title!")

        try:
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "searchInput")))

        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file("wiki_page_loading_error.png")
            driver.save_screenshot('wiki_page_loading_error.png')

        self.assertIn("Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem2 = driver.find_element(By.ID, "searchInput")
        elem2.send_keys("Earth")
        driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()

        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        # time.sleep(1)
        self.assertIn("Earth - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")
        if not "Earth" in driver.title:
            raise Exception("Wikipedia Earth page Title is wrong!")
        time.sleep(2)

        driver.find_element(By.XPATH, "//span[@class='toctext'][contains(.,'Chronology')]").click()
        self.assertIn("Earth#Chronology", driver.current_url)
        print("Get Chronology")
        if not "Earth#Chronology" in driver.current_url:
            raise Exception("Didn't get Chronology")

        driver.find_element(By.XPATH, "//span[@class='toctext'][contains(.,'Hydrosphere')]").click()
        self.assertIn("Earth#Hydrosphere", driver.current_url)
        print("Get Hydrosphere")
        if not "Earth#Hydrosphere" in driver.current_url:
            raise Exception("Didn't get Hydrosphere")

        driver.find_element(By.XPATH, "//img[@src='//upload.wikimedia.org/wikipedia/commons/thumb/9/97"
                                      "/The_Earth_seen_from_Apollo_17.jpg/220px-The_Earth_seen_from_Apollo_17.jpg']").click()

        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@title,'Show next image')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@title,'Show next image')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='mw-mmv-close']").click()

        driver.find_element(By.XPATH, "//a[@href='#cite_note-SIMEK179-31'][contains(.,'[26]')]").click()

        self.assertIn("Earth#cite_note-SIMEK179-31", driver.current_url)
        print("get footnote")
        if not "Earth#cite_note-SIMEK179-31" in driver.current_url:
            raise Exception("Didn't get footnote")

    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")
        print("Wikipedia Url has ", requests.get("https://www.wikipedia.org").status_code, " as status Code")
        code = requests.get("https://www.wikipedia.org").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")

        if not "Wikipedia" in driver.title:
            raise Exception("Wikipedia page has wrong Title!")

        time.sleep(2)

        self.assertIn("Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")

        time.sleep(2)

        driver.find_element(By.NAME, "search").click()
        driver.find_element(By.NAME, "search").send_keys("Earth")
        # elem3.send_keys("Earth")
        driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()

        time.sleep(1)
        self.assertIn("Earth - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")
        if not "Earth" in driver.title:
            raise Exception("Wikipedia Earth page Title is wrong!")
        time.sleep(2)

        driver.find_element(By.XPATH, "//span[@class='toctext'][contains(.,'Chronology')]").click()
        self.assertIn("Earth#Chronology", driver.current_url)
        print("Get Chronology")
        if not "Earth#Chronology" in driver.current_url:
            raise Exception("Didn't get Chronology")

        driver.find_element(By.XPATH, "//span[@class='toctext'][contains(.,'Hydrosphere')]").click()
        self.assertIn("Earth#Hydrosphere", driver.current_url)
        print("Get Hydrosphere")
        if not "Earth#Hydrosphere" in driver.current_url:
            raise Exception("Didn't get Hydrosphere")

        driver.find_element(By.XPATH, "//img[@src='//upload.wikimedia.org/wikipedia/commons/thumb/9/97"
                                      "/The_Earth_seen_from_Apollo_17.jpg/220px-The_Earth_seen_from_Apollo_17.jpg']").click()

        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@title,'Show next image')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@title,'Show next image')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='mw-mmv-close']").click()

        driver.find_element(By.XPATH, "//a[@href='#cite_note-SIMEK179-31'][contains(.,'[26]')]").click()

        self.assertIn("Earth#cite_note-SIMEK179-31", driver.current_url)
        print("get footnote")
        if not "Earth#cite_note-SIMEK179-31" in driver.current_url:
            raise Exception("Didn't get footnote")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))
