from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from helpers.config_parser import ApplicationConfig


app_config = ApplicationConfig()


def tap_on_add_task_field(driver):
    add_task_field_selector = "#root > div > div.App-container > div:nth-child(1) > div:nth-child(1)"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, add_task_field_selector)))
    add_task_field = driver.find_element(by=By.CSS_SELECTOR, value=add_task_field_selector)
    add_task_field.click()


def typing_task_name(driver, task_name):
    task_name_field_selector = "[id ^= 'undefined-Typetask-AddTask-']"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, task_name_field_selector)))
    task_name_field = driver.find_element(by=By.CSS_SELECTOR, value=task_name_field_selector)
    task_name_field.send_keys(task_name)


def click_on_create_button(driver):
    create_button_selector = "#root > div > div.App-container > div:nth-child(1) > div:nth-child(2) > button > div > div > span"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, create_button_selector)))
    create_button = driver.find_element(by=By.CSS_SELECTOR, value=create_button_selector)
    create_button.click()


def verify_name_of_new_task(driver, task_name):
    name_of_new_task_selector = "#root > div > div.App-container > span > div > div > div > div:nth-child(1) > div > div > div > div:nth-child(1) > div > span > div > span > div > div > div > div > label"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, name_of_new_task_selector)))
    name_of_new_task = driver.find_element(by=By.CSS_SELECTOR, value=name_of_new_task_selector)
    actual_result = name_of_new_task.text
    expected_result = task_name
    assert actual_result == expected_result


def verify_to_do_counter(driver, expected_result):
    to_do_counter_selector = "#root > div > div.App-container > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, to_do_counter_selector)))
    to_do_counter = driver.find_element(by=By.CSS_SELECTOR, value=to_do_counter_selector)
    actual_result = str(to_do_counter.text).split('(')[-1][:-1]
    assert actual_result == str(expected_result)
