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

class Test1test():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_1test(self):
    self.driver.get("http://localhost:5000/")
    self.driver.set_window_size(2286, 1261)
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    self.driver.find_element(By.LINK_TEXT, "Sentence").click()
    self.driver.find_element(By.NAME, "Sentence").click()
    self.driver.find_element(By.NAME, "Sentence").send_keys("Your are a bitch")
    self.driver.find_element(By.NAME, "Predict").click()