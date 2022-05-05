from pytest_testrail.plugin import pytestrail
from actions import create_task, change_task_state, delete_task
import string
import random

task_name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))


@pytestrail.case("C1")
def test_add_new_task_to_the_empty_board(driver):
    create_task.verify_to_do_counter(driver, 0)
    create_task.tap_on_add_task_field(driver)
    create_task.typing_task_name(driver, task_name)
    create_task.click_on_create_button(driver)
    create_task.verify_name_of_new_task(driver, task_name)
    create_task.verify_to_do_counter(driver, 1)


@pytestrail.case("C2")
def test_mark_task_as_done(driver):
    change_task_state.verify_done_counter(driver, 0)
    change_task_state.mark_new_task_as_done(driver)
    change_task_state.go_to_done_board(driver)
    change_task_state.verify_name_of_complete_task(driver, task_name)
    change_task_state.verify_done_counter(driver, 1)
    delete_task.verify_all_counter(driver, 1)


@pytestrail.case("C10")
def test_delete_all_tasks(driver):
    delete_task.verify_all_counter(driver, 1)
    delete_task.go_to_all_board(driver)
    delete_task.click_on_delete_button(driver)
    delete_task.click_on_delete_all_button(driver)
    delete_task.confirm_deletion_from_dialog(driver)
    delete_task.verify_all_counter(driver, 0)
