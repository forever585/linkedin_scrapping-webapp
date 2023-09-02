import time, random, csv
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import date, datetime
from itertools import product

class LinkedInScrapper:
    def __init__(self, parameters, driver):
        self.browser = driver
        self.email = parameters['email']
        self.password = parameters['password']
        self.profile_links = parameters['profile_links']
        self.contact_info = []

    def login(self):
        try:
            self.browser.get("https://www.linkedin.com/login")
            time.sleep(random.uniform(5, 10))
            self.browser.find_element(By.ID, "username").send_keys(self.email)
            self.browser.find_element(By.ID, "password").send_keys(self.password)
            self.browser.find_element(By.CSS_SELECTOR, ".btn__primary--large").click()
            time.sleep(random.uniform(5, 10))
        except TimeoutException:
            raise Exception("Could not login!")

    def security_check(self):
        current_url = self.browser.current_url
        page_source = self.browser.page_source

        if '/checkpoint/challenge/' in current_url or 'security check' in page_source:
            input("Please complete the security check and press enter in this console when it is done.")
            time.sleep(random.uniform(5.5, 10.5))

    def return_template(self, profile_link, email, phone_number):
        return {'email': email, 'phone_number': phone_number, 'profile_link': profile_link}

    def get_contact_info(self):


class GoogleScrapper:
    def __init__(self, parameters, driver):
        self.browser = driver
        self.parameters = parameters
        self.profile_links = []
        
    def get_profile_links(self):
        company_name = self.parameters['company_name']
        postion = self.parameters['postion']
        category = self.parameters['category']
        location = self.parameters['location']
        nof_employers = self.parameters['nof_employers']
        url = f'https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+AND+%22{company_name}%22+AND+%22{postion}%22+AND+%22{category}%22+AND+%22{location}%22+AND+%22{nof_employers}%22+%22Employers%22'
        page_number = 0
        while True:
            next_url = url + f'&start={page_number * 10}'
            try:
                self.browser.get(next_url)
                sleep(random.uniform(5, 10))
                result = self.append_profiles()
                if result == False:
                    break
            except:
                break
            page_number += 1
            print(page_number)
        return self.profile_links
    
    def append_profiles(self):
        profile_items = self.browser.find_elements(By.CLASS_NAME, 'MjjYud')
        if len(profile_items) == 0:
            return False
        item = 0
        for profile_item in profile_items:
            if item >= 10:
                break
            try:
                profile_link = profile_item.find_element(By.TAG_NAME, 'a').get_attribute('href')
                self.profile_links.append(profile_link)
            except:
                continue
            else:
                is_none = False
            item += 1
        return True
