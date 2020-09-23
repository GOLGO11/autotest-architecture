# author:yangjuntao@joinquant.com
# updateTime:2019年02月22日
from selenium import webdriver
from enum import IntEnum
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Util(object):
    '''
    Instantiated chrome object webdriver and add argument ChromeOptions(headless).
    Visit the specified web by url.
    '''
    def browser_start(self, url):
        # self.headless_option = webdriver.ChromeOptions()
        # self.headless_option.add_argument('headless')
        # self.agent_option = webdriver.ChromeOptions()
        # self.agent_option.add_argument('User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.sleep(Enum.two_time)

    '''
    close the thread of webdriver and google chrome/Ie11.
    '''
    def browser_quit(self):
        self.sleep(Enum.two_time)
        self.driver.quit()

    '''Static dormancy and the argument passed in is an integer'''
    def sleep(self, number):
        time.sleep(number)

    '''An implicit wait.'''
    def timeImplay(self,number):
        self.driver.implicitly_wait(number)

    '''refresh the web page.'''
    def browser_refresh(self):
        self.driver.refresh()

    '''
    find element by tags and attributes.
    Refresh every 0.5 seconds for a total of 30 seconds.
    '''
    def find_id(self, id):
        ids = (By.ID, id)
        WebDriverWait(self.driver, Enum.half_minute, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_element_by_id(id)

    def find_name(self, name):
        names = (By.NAME, name)
        WebDriverWait(self.driver, Enum.half_minute, Enum.half_time).until(ec.presence_of_element_located(names))
        return self.driver.find_element_by_name(name)

    def find_xpath(self, xpath):
        xpaths = (By.XPATH, xpath)
        WebDriverWait(self.driver, Enum.half_minute, Enum.half_time).until(ec.presence_of_element_located(xpaths))
        return self.driver.find_element_by_xpath(xpath)

    def find_classname(self, classname):
        classnames = (By.CLASS_NAME, classname)
        WebDriverWait(self.driver, Enum.half_minute, Enum.half_time).until(ec.presence_of_element_located(classnames))
        return self.driver.find_element_by_class_name(classname)

    def find_selector(self, selector):
        selectors = (By.CSS_SELECTOR, selector)
        WebDriverWait(self.driver, Enum.half_minute, Enum.half_time).until(ec.presence_of_element_located(selectors))
        return self.driver.find_element_by_css_selector(selector)

    def find_tag(self, tag):
        tags = (By.TAG_NAME, tag)
        WebDriverWait(self.driver, Enum.half_minute, Enum.half_time).until(ec.presence_of_element_located(tags))
        return self.driver.find_element_by_tag_name(tag)

    def find_linktext(self, link):
        texts = (By.LINK_TEXT, link)
        WebDriverWait(self.driver, Enum.half_minute, Enum.half_time).until(ec.presence_of_element_located(texts))
        return self.driver.find_element_by_link_text(link)

    def find_partial(self, partial):
        partials = (By.PARTIAL_LINK_TEXT, partial)
        WebDriverWait(self.driver, Enum.half_minute, Enum.half_time).until(ec.presence_of_element_located(partials))
        return self.driver.find_element_by_partial_link_text(partial)

    '''Click on the found element through the mouse event and the argument passed in is an integer.'''

    def click_id(self, id):
        self.find_id(id).click()

    def click_name(self, name):
        self.find_name(name).click()

    def click_xpath(self, xpath):
        self.find_xpath(xpath).click()

    def click_classname(self, classname):
        self.find_classname(classname).click()

    def click_selector(self, selector):
        self.find_selector(selector).click()

    def click_tag(self, tag):
        self.find_tag(tag).click()

    def click_linktext(self, link):
        self.find_linktext(link).click()

    def click_partial(self, partial):
        self.find_partial(partial).click()

    '''Enter text to the element that you have located'''
    def send_keys_id(self, id, message):
        self.find_id(id).send_keys(message)

    def sendkeys_name(self, name, message):
        self.find_name(name).clear()
        self.find_name(name).send_keys(message)

    def send_keys_xpath(self, xpath, message):
        self.find_xpath(xpath).send_keys(message)

    def send_keys_classname(self, classname, message):
        self.find_classname(classname).send_keys(message)

    def send_keys_selector(self, selector, message):
        self.find_selector(selector).send_keys(message)

    def send_keys_tag(self, tag, message):
        self.find_tag(tag).send_keys(message)

    def send_keys_linktext(self, link, message):
        self.find_linktext(link).send_keys(message)

    def send_keys_partial(self, partial, message):
        self.find_partial(partial).send_keys(message)

    '''Gets the text information for the element that has been located'''
    def text_id(self, id):
        return self.find_id(id).text

    def text_name(self, name):
        return self.find_name(name).text

    def text_xpath(self, xpath):
        return self.find_xpath(xpath).text

    def text_classname(self, classname):
        return self.find_classname(classname).text

    def text_selector(self, selector):
        return self.find_selector(selector).text

    def text_tag(self, tag):
        return self.find_tag(tag).text

    def text_linktext(self, link):
        return self.find_linktext(link).text

    def text_partial(self, partial):
        return self.find_partial(partial).text

    '''Gets the specified attribute of the element to which it has been located'''
    def get_attribute_id(self, id, attribute):
        return self.find_id(id).get_attribute(attribute)

    def get_attribute_xpath(self, xpath, attribute):
        return self.find_xpath(xpath).get_attribute(attribute)

    def get_attribute_selector(self, selector, attribute):
        return self.find_selector(selector).get_attribute(attribute)

    def get_atrribute_classname(self, classname, attribute):
        return self.find_classname(classname).get_attribute(attribute)

    def get_attribute_tagname(self, tagname, attribute):
        return self.find_tag(tagname).get_attribute(attribute)

    def get_attribute_partial(self, partial, attribute):
        return self.find_partial(partial).get_attribute(attribute)

    def get_attribute_name(self, name, attribute):
        return self.find_name(name).get_attribute(attribute)

    def get_attribute_linktext(self, linktext, attribute):
        return self.find_linktext(linktext).get_attribute(attribute)

    '''Switch to the popover or window that you have located.'''
    def switch_to_frame_id(self, id):
        self.driver.switch_to.frame(self.find_id(id))

    def switch_to_frame_classname(self, classname):
        self.driver.switch_to.frame(self.find_classname(classname))

    def switch_to_frame_xpath(self, xpath):
        self.driver.switch_to.frame(self.find_xpath(xpath))

    def switch_to_frame_tagname(self, tag):
        self.driver.switch_to.frame(self.find_tag(tag))

    def switch_to_frame_linktext(self, link):
        self.driver.switch_to.frame(self.find_linktext(link))

    def switch_to_frame_selector(self, selector):
        self.driver.switch_to.frame(self.find_selector(selector))

    def switch_to_frame_name(self, name):
        self.driver.switch_to.frame(self.find_name(name))

    def switch_to_frame_partail(self, partail):
        self.driver.switch_to.frame(self.find_partial(partail))

    '''Return to default window.'''
    def switch_to_content(self):
        self.driver.switch_to.default_content()

    '''Gets the current window handle.'''
    @property
    def current_window(self):
        return self.driver.current_window_handle

    '''
    get current window handle and another window handle select current window handle and switch to
    another window handle.
    '''
    def switch_to_windows(self):
        current_window = self.driver.current_window_handle
        all_window = self.driver.window_handles
        for window in all_window:
            if window != current_window:
                self.driver.switch_to_window(window)
        print("Switch to New Window")

    def switch_to_current_window(self, current_window):
        all_window = self.driver.window_handles
        for window in all_window:
            if window == current_window:
                self.driver.switch_to_window(window)
        print('Switch to Current Window')

    '''
    select a group of elements with xml path or id or name or classname or linetext or other attribute.
    '''
    def find_group_id(self, id):
        ids = (By.ID, id)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_id(id)

    def click_group_id(self, id, index):
        self.find_group_id(id)[index].click()

    def send_keys_group_id(self, id, index, message):
        self.find_group_id(id)[index].send_keys(message)

    def text_group_id(self, id, index):
        return self.find_group_id(id)[index].text

    def find_group_xpath(self, xpath):
        ids = (By.XPATH, xpath)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_xpath(xpath)

    def click_group_xpath(self, index, xpath):
        self.find_group_xpath(xpath)[index].click()

    def send_keys_group_xpath(self, index, xpath, message):
        self.find_group_xpath(xpath)[index].send_keys(message)

    def text_group_xpath(self, index, xpath):
        return self.find_group_xpath(xpath)[index].text

    def find_group_classname(self, classname):
        ids = (By.CLASS_NAME, classname)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_class_name(classname)

    def click_group_classname(self, classname, index):
        self.find_group_classname(classname)[index].click()

    def send_keys_group_classname(self, classname, index, message):
        self.find_group_classname(classname)[index].send_keys(message)

    def text_group_classname(self, index, classname):
        return self.find_group_classname(classname)[index].text

    def find_group_selector(self, selector):
        ids = (By.CSS_SELECTOR, selector)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_css_selector(selector)

    def click_group_selector(self, selector, index):
        self.find_group_selector(selector)[index].click()

    def send_keys_group_selector(self, selector, index, message):
        self.find_group_selector(selector)[index].send_keys(message)

    def text_group_selector(self, selector, index):
        return self.find_group_selector(selector)[index].text

    def find_group_linktext(self, link):
        ids = (By.LINK_TEXT, link)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_link_text(link)

    def click_group_linktext(self, link, index):
        self.find_group_linktext(link)[index].click()

    def send_keys_group_linktext(self, link, index, message):
        self.find_group_linktext(link)[index].send_keys(message)

    def text_group_linktext(self, link, index):
        return self.find_group_linktext(link)[index].text

    def find_group_partial(self, partial):
        ids = (By.PARTIAL_LINK_TEXT, partial)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_partial_link_text(partial)

    def click_group_partial(self, partial, index):
        self.find_group_partial(partial)[index].click()

    def send_keys_group_partial(self, partial, index, message):
        self.find_group_partial(partial)[index].send_keys(message)

    def text_group_partial(self, partial, index):
        return self.find_group_partial(partial)[index].text

    def find_group_tag(self, tag):
        ids = (By.TAG_NAME, tag)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_tag_name(tag)

    def click_group_tag(self, tag, index):
        self.find_group_tag(tag)[index].click()

    def send_keys_group_tag(self, tag, index, message):
        self.find_group_tag(tag)[index].send_keys(message)

    def text_group_tag(self, tag, index):
        return self.find_group_tag(tag)[index].text

    def find_group_name(self, name):
        names = (By.NAME, name)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(names))
        return self.driver.find_elements_by_name(name)

    def click_group_name(self, name, index):
        self.find_group_name(name)[index].click()

    def sendkeys_group_name(self, name, index, message):
        self.find_group_name(name)[index].send_keys(message)

    def text_group_name(self, name, index):
        return self.find_group_name(name)[index].text

    '''Gets current url.'''
    @property
    def current_url(self):
        return self.driver.current_url

    '''Gets the title of current html.'''
    def get_title(self):
        return self.driver.title

    '''back to the before web.'''
    def url_back(self):
        self.driver.back()

    '''Keyboard events.'''
    def id_enter(self, id):
        self.find_id(id).send_keys(Keys.ENTER)

    def name_enter(self, name):
        self.find_name(name).send_keys(Keys.ENTER)

    def classname_enter(self, classname):
        self.find_classname(classname).send_keys(Keys.ENTER)

    def tag_enter(self, tagname):
        self.find_tag(tagname).send_keys(Keys.ENTER)

    def xpath_enter(self, xpath):
        self.find_xpath(xpath).send_keys(Keys.ENTER)

    def selector_enter(self, selector):
        self.find_selector(selector).send_keys(Keys.ENTER)

    def linktext_enter(self, linktext):
        self.find_linktext(linktext).send_keys(Keys.ENTER)

    def partail_enter(self, partail):
        self.find_partial(partail).send_keys(Keys.ENTER)

    def id_tab(self, id):
        self.find_id(id).send_keys(Keys.TAB)

    def name_tab(self, name):
        self.find_name(name).send_keys(Keys.TAB)

    def classname_tab(self, classname):
        self.find_classname(classname).send_keys(Keys.TAB)

    def tag_tab(self, tagname):
        self.find_tag(tagname).send_keys(Keys.TAB)

    def xpath_tab(self, xpath):
        self.find_xpath(xpath).send_keys(Keys.TAB)

    def selector_tab(self, selector):
        self.find_selector(selector).send_keys(Keys.TAB)

    def linktext_tab(self, linktext):
        self.find_linktext(linktext).send_keys(Keys.TAB)

    def partail_tab(self, partail):
        self.find_partial(partail).send_keys(Keys.TAB)

    def id_copy(self, id):
        self.find_id(id).send_keys(Keys.CONTROL, 'c')

    def name_copy(self, name):
        self.find_name(name).send_keys(Keys.CONTROL, 'c')

    def classname_copy(self, classname):
        self.find_classname(classname).send_keys(Keys.CONTROL, 'c')

    def tag_copy(self, tagname):
        self.find_tag(tagname).send_keys(Keys.CONTROL, 'c')

    def xpath_copy(self, xpath):
        self.find_xpath(xpath).send_keys(Keys.CONTROL, 'c')

    def selector_copy(self, selector):
        self.find_selector(selector).send_keys(Keys.CONTROL, 'c')

    def linktext_copy(self, linktext):
        self.find_linktext(linktext).send_keys(Keys.CONTROL, 'c')

    def partail_copy(self, partail):
        self.find_partial(partail).send_keys(Keys.CONTROL, 'c')

    def id_stick(self, id):
        self.find_id(id).send_keys(Keys.CONTROL, 'v')

    def name_stick(self, name):
        self.find_name(name).send_keys(Keys.CONTROL, 'v')

    def classname_stick(self, classname):
        self.find_classname(classname).send_keys(Keys.CONTROL, 'v')

    def tag_stick(self, tagname):
        self.find_tag(tagname).send_keys(Keys.CONTROL, 'v')

    def xpath_stick(self, xpath):
        self.find_xpath(xpath).send_keys(Keys.CONTROL, 'v')

    def selector_stick(self, selector):
        self.find_selector(selector).send_keys(Keys.CONTROL, 'v')

    def linktext_stick(self, linktext):
        self.find_linktext(linktext).send_keys(Keys.CONTROL, 'v')

    def partail_stick(self, partail):
        self.find_partial(partail).send_keys(Keys.CONTROL, 'v')

    def id_all(self, id):
        self.find_id(id).send_keys(Keys.CONTROL, 'a')

    def name_all(self, name):
        self.find_name(name).send_keys(Keys.CONTROL, 'a')

    def classname_all(self, classname):
        self.find_classname(classname).send_keys(Keys.CONTROL, 'a')

    def tag_all(self, tagname):
        self.find_tag(tagname).send_keys(Keys.CONTROL, 'a')

    def xpath_all(self, xpath):
        self.find_xpath(xpath).send_keys(Keys.CONTROL, 'a')

    def selector_all(self, selector):
        self.find_selector(selector).send_keys(Keys.CONTROL, 'a')

    def linktext_all(self, linktext):
        self.find_linktext(linktext).send_keys(Keys.CONTROL, 'a')

    def partail_all(self, partail):
        self.find_partial(partail).send_keys(Keys.CONTROL, 'a')

    '''Mouse events.'''
    def move_id(self, id):
        ActionChains(self.driver).move_to_element(self.find_id(id)).perform()

    def move_name(self, name):
        ActionChains(self.driver).move_to_element(self.find_name(name)).perform()

    def move_classname(self, classname):
        ActionChains(self.driver).move_to_element(self.find_classname(classname)).perform()

    def move_tagname(self, tagname):
        ActionChains(self.driver).move_to_element(self.find_tag(tagname)).perform()

    def move_xpath(self, xpath):
        ActionChains(self.driver).move_to_element(self.find_xpath(xpath)).perform()

    def move_selector(self, selector):
        ActionChains(self.driver).move_to_element(self.find_selector(selector)).perform()

    def move_linktext(self, linktext):
        ActionChains(self.driver).move_to_element(self.find_linktext(linktext)).perform()

    def move_partail(self, partail):
        ActionChains(self.driver).move_to_element(self.find_partial(partail)).perform()

    def context_click_id(self, id):
        ActionChains(self.driver).context_click(self.find_id(id)).perform()

    def context_click_name(self, name):
        ActionChains(self.driver).context_click(self.find_name(name)).perform()

    def context_click_classname(self, classname):
        ActionChains(self.driver).context_click(self.find_classname(classname)).perform()

    def context_click_tagname(self, tagname):
        ActionChains(self.driver).context_click(self.find_tag(tagname)).perform()

    def context_click_xpath(self, xpath):
        ActionChains(self.driver).context_click(self.find_xpath(xpath)).perform()

    def context_click_selector(self, selector):
        ActionChains(self.driver).context_click(self.find_selector(selector)).perform()

    def context_click_partail(self, partail):
        ActionChains(self.driver).context_click(self.find_partial(partail)).perform()

    def context_click_linktext(self, linktext):
        ActionChains(self.driver).context_click(self.find_linktext(linktext)).perform()

    def double_click_id(self, id):
        ActionChains(self.driver).double_click(self.find_id(id)).perform()

    def doubile_click_name(self, name):
        ActionChains(self.driver).double_click(self.find_name(name)).perform()

    def double_click_tagname(self, tagname):
        ActionChains(self.driver).double_click(self.find_tag(tagname)).perform()

    def double_click_classname(self, classname):
        ActionChains(self.driver).double_click(self.find_classname(classname)).perform()

    def double_click_linktext(self, linktext):
        ActionChains(self.driver).double_click(self.find_linktext(linktext)).perform()

    def double_click_xpath(self, xpath):
        ActionChains(self.driver).double_click(self.find_xpath(xpath)).perform()

    def double_click_selectorr(self, selector):
        ActionChains(self.driver).double_click(self.find_selector(selector)).perform()

    def double_click_partail(self, partail):
        ActionChains(self.driver).double_click(self.find_partial(partail)).perform()

    def select_id(self, select_id, context_id):
        self.move_id(self.find_id(select_id))
        self.click_id(self.find_id(context_id))

    def select_name(self, select_name, context_name):
        self.move_name(self.find_name(select_name))
        self.click_name(self.find_id(context_name))

    def select_classname(self, select_classname, context_classname):
        self.move_classname(self.find_classname(select_classname))
        self.click_classname(self.find_classname(context_classname))

    def select_tagname(self, select_tagname, context_tagname):
        self.move_tagname(self.find_tag(select_tagname))
        self.click_tag(self.find_tag(context_tagname))

    def select_xpath(self, select_xpath, context_xpath):
        self.move_xpath(self.find_xpath(select_xpath))
        self.click_xpath(self.find_xpath(context_xpath))

    def select_selector(self, select_selector, context_selector):
        self.move_selector(self.find_selector(select_selector))
        self.click_selector(self.find_selector(context_selector))

    def select_linktext(self, select_linktext,context_linktext):
        self.move_linktext(self.find_linktext(select_linktext))
        self.click_linktext(self.find_linktext(context_linktext))

    def select_partail(self, select_partail, context_partail):
        self.move_partail(self.find_partial(select_partail))
        self.click_partial(self.find_partial(context_partail))

    def select_text_id(self, select_id, context_id):
        self.move_id(self.find_id(select_id))
        self.text_id(self.find_id(context_id))

    def select_text_name(self, select_name, context_name):
        self.move_name(self.find_name(select_name))
        self.text_name(self.find_name(context_name))

    def select_text_classname(self, select_classname, context_classname):
        self.move_classname(self.find_classname(select_classname))
        self.text_classname(self.find_classname(context_classname))

    def select_text_tagname(self, select_tagname, context_tagname):
        self.move_tagname(self.find_tag(select_tagname))
        self.text_tag(self.find_tag(context_tagname))

    def select_text_xpath(self, select_xpath, context_xpath):
        self.move_xpath(self.find_xpath(select_xpath))
        self.text_xpath(self.find_xpath(context_xpath))

    def select_text_selector(self, select_selector, context_selector):
        self.move_selector(self.find_selector(select_selector))
        self.text_selector(self.find_selector(context_selector))

    def select_text_linktext(self, select_linktext, context_linktext):
        self.move_linktext(self.find_linktext(select_linktext))
        self.text_linktext(self.find_linktext(context_linktext))

    def select_text_partail(self, select_partail, context_partail):
        self.move_partail(self.find_partial(select_partail))
        self.text_partial(self.find_partial(context_partail))

    def select_context_id(self, select_id, index):
        Select(self.find_id(select_id)).select_by_index(index)

    def select_context_name(self, select_name, index):
        Select(self.find_name(select_name)).select_by_index(index)

    def select_context_classname(self, select_classname, index):
        Select(self.find_classname(select_classname)).select_by_index(index)

    def select_context_tagname(self, select_tagname, index):
        Select(self.find_tag(select_tagname)).select_by_index(index)

    def select_context_xpath(self, select_xpath, index):
        Select(self.find_xpath(select_xpath)).select_by_index(index)

    def select_context_selector(self, select_selector, index):
        Select(self.find_selector(select_selector)).select_by_index(index)

    def select_context_linktext(self, select_linktext, index):
        Select(self.find_linktext(select_linktext)).select_by_index(index)

    def select_context_partail(self, select_partail, index):
        Select(self.find_partial(select_partail)).select_by_index(index)

    def select_value_id(self, value_id, value):
        Select(self.find_id(value_id)).select_by_value(value)

    def select_value_name(self, value_name, value):
        Select(self.find_name(value_name)).select_by_value(value)

    def select_value_classname(self, value_classname, value):
        Select(self.find_classname(value_classname)).select_by_value(value)

    def select_value_tagname(self, value_tagname, value):
        Select(self.find_tag(value_tagname)).select_by_value(value)

    def select_value_xpath(self, value_xpath, value):
        Select(self.find_xpath(value_xpath)).select_by_value(value)

    def select_value_selector(self, value_selector, value):
        Select(self.find_selector(value_selector)).select_by_value(value)

    def select_value_linktext(self, value_linktext, value):
        Select(self.find_linktext(value_linktext)).select_by_value(value)

    def select_value_partail(self, value_partail, value):
        Select(self.find_partial(value_partail)).select_by_value(value)

    def get_screen(self, nowtime):
        self.driver.get_screenshot_as_file("%s.jpg"% nowtime)

    def is_element_exist_id(self, id):
        self.count = self.driver.find_elements_by_id(id)
        if len(self.count) == 0:
            print("元素未找到%s" % id)
        elif len(self.count) == 1:
            return True
        else:
            print("找到%s个元素" % len(self.count))
            return False

    def is_element_exist_name(self, name):
        self.count = self.driver.find_elements_by_id(name)
        if len(self.count) == 0:
            print("元素未找到%s" % name)
        elif len(self.count) == 1:
            return True
        else:
            print("找到%s个元素" % len(self.count))
            return False

    def is_element_exist_classname(self, classname):
        self.count = self.driver.find_elements_by_id(classname)
        if len(self.count) == 0:
            print("元素未找到%s" % classname)
        elif len(self.count) == 1:
            return True
        else:
            print("找到%s个元素" % len(self.count))
            return False

    def is_element_exist_tagname(self, tagname):
        self.count = self.driver.find_elements_by_id(tagname)
        if len(self.count) == 0:
            print("元素未找到%s" % tagname)
        elif len(self.count) == 1:
            return True
        else:
            print("找到%s个元素" % len(self.count))
            return False

    def is_element_exist_xpath(self, xpath):
        self.count = self.driver.find_elements_by_id(xpath)
        if len(self.count) == 0:
            print("元素未找到%s" % xpath)
        elif len(self.count) == 1:
            return True
        else:
            print("找到%s个元素" % len(self.count))
            return False

    def is_element_exist_selector(self, selector):
        self.count = self.driver.find_elements_by_id(selector)
        if len(self.count) == 0:
            print("元素未找到%s" % selector)
        elif len(self.count) == 1:
            return True
        else:
            print("找到%s个元素" % len(self.count))
            return False

    def is_element_exist_linktext(self, text):
        self.count = self.driver.find_elements_by_id(text)
        if len(self.count) == 0:
            print("元素未找到%s" % text)
        elif len(self.count) == 1:
            return True
        else:
            print("找到%s个元素" % len(self.count))
            return False

    def is_element_exist_partail(self, partail):
        self.count = self.driver.find_elements_by_id(partail)
        if len(self.count) == 0:
            print("元素未找到%s" % partail)
        elif len(self.count) == 1:
            return True
        else:
            print("找到%s个元素" % len(self.count))
            return False

    def alert_id(self, id):
        self.click_id(id)
        self.driver.switch_to_alert().accept()

    def alert_name(self, name):
        self.click_name(name)
        self.driver.switch_to_alert().accept()

    def alert_classname(self, classname):
        self.click_classname(classname)
        self.driver.switch_to_alert().accept()

    def alert_tagname(self, tagname):
        self.click_tag(tagname)
        self.driver.switch_to_alert().accept()

    def alert_xpath(self, xpath):
        self.click_xpath(xpath)
        self.driver.switch_to_alert().accept()

    def alert_selector(self, selector):
        self.click_selector(selector)
        self.driver.switch_to_alert().accept()

    def alert_linktext(self, text):
        self.click_linktext(text)
        self.driver.switch_to_alert().accept()

    def alert_partail(self, partail):
        self.click_partial(partail)
        self.driver.switch_to_alert().accept()

    def accpet_id(self, id):
        self.click_id(id)
        self.driver.switch_to_alert().accept()

    def accpet_name(self, name):
        self.click_name(name)
        self.driver.switch_to_alert().accept()

    def accept_classname(self, classname):
        self.click_classname(classname)
        self.driver.switch_to_alert().accept()

    def accept_tagname(self, tagname):
        self.click_tag(tagname)
        self.driver.switch_to_alert().accept()

    def accpet_xpath(self, xpath):
        self.click_xpath(xpath)
        self.driver.switch_to_alert().accept()

    def accept_selector(self, selector):
        self.click_selector(selector)
        self.driver.switch_to_alert().accept()

    def accept_linktext(self, text):
        self.click_linktext(text)
        self.driver.switch_to_alert().accept()

    def accept_partail(self, partail):
        self.click_partial(partail)
        self.driver.switch_to_alert().accept()

    def dismiss_id(self, id):
        self.click_id(id)
        self.driver.switch_to_alert().dismiss()

    def dismiss_name(self, name):
        self.click_name(name)
        self.driver.switch_to_alert().dismiss()

    def dismiss_classname(self, classname):
        self.click_classname(classname)
        self.driver.switch_to_alert().dismiss()

    def dismiss_tagname(self, tagname):
        self.click_tag(tagname)
        self.driver.switch_to_alert().dismiss()

    def dismiss_xpath(self, xpath):
        self.click_xpath(xpath)
        self.driver.switch_to_alert().dismiss()

    def dismiss_selector(self, selector):
        self.click_selector(selector)
        self.driver.switch_to_alert().dismiss()

    def dismiss_linktext(self, text):
        self.click_linktext()
        self.driver.switch_to_alert().dismiss()

    def dismiss_partail(self, partail):
        self.click_partial(partail)
        self.driver.switch_to_alert().dismiss()

    def prompt_accept_id(self, id, message):
        self.click_id(id)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.accept()

    def prompt_accept_name(self, name, message):
        self.click_name(name)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.accept()

    def prompt_accept_classname(self, classname, message):
        self.click_classname(classname)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.accept()

    def prompt_accept_tagname(self, tagname, message):
        self.click_tag(tagname)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.accept()

    def prompt_accept_xpath(self, xpath, message):
        self.click_xpath(xpath)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.accept()

    def prompt_accept_selector(self, selector, message):
        self.click_selector(selector)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.accept()

    def prompt_accept_linktext(self, text, message):
        self.click_linktext(text)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.accept()

    def prompt_accept_partail(self, partail, message):
        self.click_partial(partail)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.accept()

    def prompt_dismiss_id(self, id, message):
        self.click_id(id)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.dismiss()

    def prompt_dismiss_name(self, name, message):
        self.click_name(name)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.dismiss()

    def prompt_dismiss_classname(self, classname, message):
        self.click_classname(classname)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.dismiss()

    def prompt_dismiss_tagname(self, tagname, message):
        self.click_tag(tagname)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.dismiss()

    def prompt_dismiss_xpath(self, xpath, message):
        self.click_xpath(xpath)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.dismiss()

    def prompt_dismiss_selector(self, selector, message):
        self.click_selector(selector)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.dismiss()

    def prompt_dismiss_linktext(self, text, message):
        self.click_linktext(text)
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.dismiss()

    def prompt_dismiss_partail(self, partail, message):
        self.prompt = self.driver.switch_to_alert()
        self.prompt.send_keys(message)
        self.prompt.dismiss()

    def clear_input(self, xpath):
        self.find_xpath(xpath).clear()

    def all_windows(self):
        print(self.driver.window_handles)
        return self.driver.window_handles

    def browser_closed(self):
        self.sleep(2)
        self.driver.close()

    '''
    Used to attribution except "Input" to send text or file
    if you use it please don't use mouse to click anything in browser
    '''
    def pre_input_xpath(self, xpath, message):
        ActionChains(self.driver).click(self.find_xpath(xpath)).send_keys(message).perform()

    def pre_input_id(self, id, message):
        ActionChains(self.driver).click(self.find_id(id)).send_keys(message).perform()

    def pre_input_name(self, name, message):
        ActionChains(self.driver).click(self.find_name(name)).send_keys(message).perform()

    def pre_input_classname(self, classname, message):
        ActionChains(self.driver).click(self.find_classname(classname)).send_keys(message).perform()

    def pre_input_tagname(self, tagname, message):
        ActionChains(self.driver).click(self.find_tag(tagname)).send_keys(message).perform()

    def pre_input_selector(self, selector, message):
        ActionChains(self.driver).click(self.find_selector(selector)).send_keys(message).perform()

    def pre_input_linktext(self, link, message):
        ActionChains(self.driver).click(self.find_linktext(link)).send_keys(message).perform()

    def pre_input_partail(self, partail, message):
        ActionChains(self.driver).click(self.find_partial(partail)).send_keys(message).perform()

    def move_by_offset(self, xoffset, yoffset):
        ActionChains(self.driver).move_by_offset(xoffset, yoffset)


'''A class for Number Enumeration between 0.1 and 100.'''
class Enum(IntEnum):
    point_one_time = 0.1
    half_time = 0.5
    one_time = 1
    two_time = 2
    three_time = 3
    five_time = 5
    ten_time = 10
    twenty_time = 20
    half_minute = 30
    fifty_time = 50
    hundred_time = 100


