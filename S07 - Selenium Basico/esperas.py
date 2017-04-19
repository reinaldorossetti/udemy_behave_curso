from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException


def xpath_presence_of_element_located(driver, elem, timeout=60):
    # self.FindFrame(driver)
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, elem)))
        return element
    except NoSuchElementException:
        raise Exception("Except Element not found!")


def xpath_element_to_be_clickable(driver, elem, timeout=60):
    # self.FindFrame(driver)
    try:
        element = WebDriverWait(driver, timeout, poll_frequency=0.1).until(
            EC.element_to_be_clickable((By.XPATH, elem)))
        return element
    except NoSuchElementException:
        raise Exception("Except Element not found!")


def fluentwait(driver, elem, timeout=60):
    # self.FindFrame(driver)
    try:
        element = WebDriverWait(driver, timeout, poll_frequency=1,
                                ignored_exceptions=[ElementNotVisibleException,
                                                    ElementNotSelectableException]).until(
            EC.element_to_be_clickable((By.XPATH, elem)))
        return element
    except NoSuchElementException:
        raise Exception("Except Element not found!")
