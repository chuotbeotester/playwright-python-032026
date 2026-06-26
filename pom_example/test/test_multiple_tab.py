from page.Orange.orange_login_page import LoginOrange
from page.Orange.linked_page import Linked
import time

def test_open_linked_tab(page):
    orange = LoginOrange(page)
    orange.navigate_to_orange_page()
    linked = Linked(page)
    linked = orange.click_open_linked_page()
    linked.assert_is_linked_page()
    linked._page_close()
    time.sleep(2)
    orange.login()
    orange._bring_to_front()
    # time.sleep(3)
    # linked._bring_to_front()
    # time.sleep(3)
