import unittest

class test_case():

    def test_login_1(self):
        '''
        test_case description
        '''
        self.login_in()
        self.util.sleep(1)
        self.new_url = self.util.current_url
        '''
        from login page to next page
        '''
        self.assertEqual(self.new_url, self.config.floor_url)
        self.util.sleep(1)
        self.util.move_xpath(Source._move_1)
        self.login_out()
        self.log.info('new_url '+ self.new_url)
