# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class TestSmokeTest():
   def setup_method(self, method):
        options = Options()
        options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/google-chrome-stable")
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(executable_path=os.getenv("CHROMEDRIVER_BIN", "/usr/bin/chromedriver"), options=options)
        self.vars = {}

  def teardown_method(self, method):
        self.driver.quit()
        
  def test_adminPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1296, 1400)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Username:"
    element = self.driver.find_element(By.ID, "username")
    assert element.is_enabled() is True
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.ID, "password").send_keys("adin123213")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".errorMessage").text == "Invalid username and password."
  
  def test_directoryPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(2560, 1400)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
  
  def test_homePage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(2576, 1416)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    elements = self.driver.find_elements(By.LINK_TEXT, "Join")
    assert len(elements) > 0
  
  def test_joinPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1296, 1400)
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "First Name"
    self.driver.find_element(By.NAME, "fname").click()
    element = self.driver.find_element(By.NAME, "fname")
    assert element.is_enabled() is True
    self.driver.find_element(By.NAME, "fname").click()
    self.driver.find_element(By.NAME, "fname").send_keys("Gianfranco")
    self.driver.find_element(By.NAME, "lname").send_keys("Gosdinski")
    self.driver.find_element(By.NAME, "bizname").send_keys("ASPERSUD")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("sd")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.NAME, "email").click()
    element = self.driver.find_element(By.NAME, "email")
    assert element.is_enabled() is True
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Email"
  
