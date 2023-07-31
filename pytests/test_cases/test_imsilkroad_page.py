

import allure

from pytests.test_steps.imsilkroad_steps import *


# @allure.issue("JIRA-003")
# @allure.description("verify user can login successfully")
# def test_with_issue(imsilkroad_page):
#     login_to_imsilkroad(imsilkroad_page)

@allure.issue("JIRA-004")
@allure.description("verify user can get result data")
def test_with_issue_2(imsilkroad_page):
    login_to_imsilkroad(imsilkroad_page)
    time.sleep(30)
    fill_search_filters(imsilkroad_page)
    get_search_result(imsilkroad_page)
