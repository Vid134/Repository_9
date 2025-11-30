import pytest                  ##imports pytest framework for writing and running tests
from selenium import webdriver  ##imports selenium webdriver to automate the browser
from selenium.webdriver.common.by import By   ##this imports By class from selenium webdriver,this also tells which locators to use
import time                      ##to import the built-in time module


 ##Fixtures in Pytest are used to set up a consistent and reusable test environment.
##They help in preparing the necessary preconditions for tests and can also handle cleanup after tests are executed.

@pytest.fixture   ##Pytest automatically invokes the fixture before executing the test.
def website_setup():   ##function to start browser and open website
    driver = webdriver.Chrome()    ##launches chrome browser instance
    driver.maximize_window()       ##for better visibility it maximizes the browser window
    driver.get("https://www.guvi.in/")   ##opens guvi website homepage
    yield driver                    ##returns driver instance to the test function for use
    print("Fixture Executed")        ##prints message once test completes
    time.sleep(2)                       #waits before closing the browser
    driver.quit()                      ##closes the browser window and ends the session

def test_parent_first_child(website_setup):     ##test case to validate parent and first child xpath
    driver = website_setup                        ##uses browser instance from fixture
    parent_courses = driver.find_element(By.XPATH, "//a[text()='Courses']/parent::*")           # Locates the parent element using xpath
    assert parent_courses                              ##asserts that element is found successful

    first_child = driver.find_element(By.XPATH, "//a[text()='Courses']/parent::*/*[1]")        # Locates First child of parent element
    assert first_child                                           ##asserts that element is found successful

def test_second_sibling(website_setup):         ##test case to validate second sibling xpath
    driver = website_setup                        ##uses browser instance from fixture
    second_siblings = driver.find_element(By.XPATH, "//a[text()='Courses']/following-sibling::*[2]")   ## Locates the sibling element using xpath
    assert second_siblings                                                    ##asserts that element is found successful

def test_parent_href(website_setup):                  ##test case to validate parent element from href attribute
    driver = website_setup                              ##uses browser instance from fixture
    href_parent = driver.find_element(By.XPATH, "//link[@href='https://www.guvi.in/']/parent::*")      ## parent element from href attribute
    assert href_parent                                                    ##asserts that element is found successful

def test_ancestor_elements(website_setup):               ##test case to validate ancestors xpath
    driver = website_setup                                    ##uses browser instance from fixture
    ancestor = driver.find_elements(By.XPATH, "//a[text()='Courses']/ancestor::div")       ## Locates the ancestor element using xpath
    assert ancestor                                                  ##asserts that element is found successful

def test_following_siblings(website_setup):                ##test case to validate following siblings xpath
    driver = website_setup                                     #uses browser instance from fixture
    following_siblings = driver.find_elements(By.XPATH, "//a[text()='Courses']/following-sibling::hr")              ## Locates the folowing siblings element using xpath
    assert following_siblings                                       ##asserts that element is found successful

def test_preceding_elements(website_setup):         ##test case to validate preceeding elements xpath
    driver = website_setup                          #uses browser instance from fixture
    preceding = driver.find_elements(By.XPATH, "//a[@href='/courses']/preceding::*")      ## Locates the preceeding element using xpath
    assert preceding                                              ##asserts that element is found successful