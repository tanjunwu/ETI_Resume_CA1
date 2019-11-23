from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

driver=webdriver.Chrome()

def test_homepage():
    driver.get('http://127.0.0.1:8000/')
    assert "Home" in driver.title

def test_blogpage():
    driver.get('http://127.0.0.1:8000/blog/')
    assert "My Blog" in driver.title
    
def test_adminpage():
    driver.get('http://127.0.0.1:8000/admin/')
    assert "Log in | Django site admin" in driver.title
    
def test_wrong_port_number():
    driver.get('http://127.0.0.1:8066/blog/')
    assert "127.0.0.1" in driver.title
    
def test_unknown_page():
    driver.get('http://127.0.0.1:8000/friends')
    assert "Page not found at /friends" in driver.title
