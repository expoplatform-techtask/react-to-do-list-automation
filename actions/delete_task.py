from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from helpers.config_parser import ApplicationConfig


app_config = ApplicationConfig()


def go_to_all_board(driver):
    all_board_selector = "#root > div > div.App-container > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(3)"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, all_board_selector)))
    all_board = driver.find_element(by=By.CSS_SELECTOR, value=all_board_selector)
    all_board.click()


def click_on_delete_button(driver):
    delete_button_selector = "#root > div > div.enable-remove-mode > div > button"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, delete_button_selector)))
    delete_button = driver.find_element(by=By.CSS_SELECTOR, value=delete_button_selector)
    delete_button.click()


def click_on_delete_all_button(driver):
    delete_all_button_selector = "#root > div > div.App-container > span > div.remove-mode > div > button"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, delete_all_button_selector)))
    delete_all_button = driver.find_element(by=By.CSS_SELECTOR, value=delete_all_button_selector)
    delete_all_button.click()


def confirm_deletion_from_dialog(driver):
    dialog_delete_button_selector = "body > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(3) > button:nth-child(2)"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, dialog_delete_button_selector)))
    dialog_delete_button = driver.find_element(by=By.CSS_SELECTOR, value=dialog_delete_button_selector)
    dialog_delete_button.click()


def verify_all_counter(driver, expected_result):
    all_counter_selector = "#root > div > div.App-container > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(3)"
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, all_counter_selector)))
    all_counter = driver.find_element(by=By.CSS_SELECTOR, value=all_counter_selector)
    actual_result = str(all_counter.text).split('(')[-1][:-1]
    assert actual_result == str(expected_result)
