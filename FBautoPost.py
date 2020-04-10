from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
import unittest
import HTMLTestRunner

chrome_path = 'C:/selenium_driver_chrome/chromedriver.exe'  # path of chromedriver.exe
current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
url = 'https://www.facebook.com/login'

chrome_options = Options()
options = webdriver.ChromeOptions()  # 防止chrome正在受到自動化測試通知
options.add_argument('disable-infobars')
prefs = {
    'profile.default_content_setting_values':  # 屏蔽chrome通知
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)


class Autopost(unittest.TestCase):
    # initial setting
    def setUp(self):
        self.driver = webdriver.Chrome(chrome_path, options=options)

    def test_postArticle(self):
        # noinspection PyBroadException
        flag = True
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            sleep(2)
            self.driver.find_element_by_id('email').send_keys('mybooktest0604@gmail.com')  # add your account here
            self.driver.find_element_by_id('pass').send_keys('twm09350935')  # add your password here
            sleep(2)
            self.driver.find_element_by_id("loginbutton").click()
            sleep(5)
            self.driver.find_element_by_partial_link_text('首頁').click()
            sleep(3)
            self.driver.find_element_by_class_name('_3en1').send_keys(
                '%s : ' 
                'Test~Test~Test~Test~Test~Test~Jenkins!!\n'
                'IIT : http://www.iit.com.hk/'

            % current_time)
            sleep(7)
            self.driver.find_element_by_class_name('_1mf7').click()
            sleep(3)
            js = "var q=document.documentElement.scrollTop=200"  # scroll to bottom
            self.driver.execute_script(js)
            sleep(30)

        except:
            flag = False
            if flag is False:
                self.driver.save_screenshot('C:/Users/jack.tsao/PycharmProjects/PythonAutomation/scrpath/autoPostFail_%s.png' % current_time)
                self.assertTrue(flag, 'Execute Fail.')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    filepath = (r'C:\Users\jack.tsao\PycharmProjects\PythonAutomation\report\autoPostReport_%s.html' % current_time)
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(Autopost('test_postArticle'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='AutoPost Test Report')
    runner.run(suite)
