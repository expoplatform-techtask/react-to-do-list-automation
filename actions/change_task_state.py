from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from helpers.config_parser import ApplicationConfig


app_config = ApplicationConfig()


def mark_new_task_as_done(driver):
    new_task_selector = "#root > div > div.App-container > span > div > div > div > div:nth-child(1) > div > div > div > div:nth-child(1) > div > span > div > span > div > div"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, new_task_selector)))
    new_task = driver.find_element(by=By.CSS_SELECTOR, value=new_task_selector)
    new_task.click()


def go_to_done_board(driver):
    done_board_selector = "#root > div > div.App-container > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(2)"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, done_board_selector)))
    done_board = driver.find_element(by=By.CSS_SELECTOR, value=done_board_selector)
    done_board.click()


def verify_name_of_complete_task(driver, task_name):
    name_of_complete_task_selector = "#root > div > div.App-container > span > div > div > div > div:nth-child(2) > div > div > div > div:nth-child(1) > div > span > div > span > div > div > div > div > label"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, name_of_complete_task_selector)))
    name_of_complete_task = driver.find_element(by=By.CSS_SELECTOR, value=name_of_complete_task_selector)
    actual_result = name_of_complete_task.text
    expected_result = task_name
    assert actual_result == expected_result


def verify_done_counter(driver, expected_result):
    done_counter_selector = "#root > div > div.App-container > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(2)"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, done_counter_selector)))
    done_counter = driver.find_element(by=By.CSS_SELECTOR, value=done_counter_selector)
    actual_result = str(done_counter.text).split('(')[-1][:-1]
    assert actual_result == str(expected_result)
