from base_test import TestBase
from time import sleep

class TestFeature(TestBase):
    def test_start_script(self):
        self.start_page.check_ip()

        self.base_page.intoli_com()


        # self.start_page.open_beehance()
        # self.start_page.click_button_piple()
        # self.start_page.enter_text_into_search()
        # self.searching_results.check_and_click_user_card()
        # sleep(2)
        # self.user_profile.go_too_content_page()
        # self.content_page.click_like()




        sleep(5)

