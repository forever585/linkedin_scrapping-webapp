import os, random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from scrapper import LinkedInScrapper, GoogleScrapper
from flask import Flask, redirect, render_template, request, url_for
from time import sleep

app = Flask(__name__)

linkedin_email = os.getenv("LINKEDIN_EMAIL")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")

binary_location =  os.getenv("CHROMER_LOCATION")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        google_paramerters = {
            'company_name' : request.form['company_name'],
            'postion' : request.form['postion'],
            'category' : request.form['category'],
            'location' : request.form['location'],
            'nof_employers' : request.form['nof_employers'],
        }
        profile_links = get_profile_links(google_paramerters)

        linkedin_parameters = {
            'email': linkedin_email,
            'password': linkedin_password,
            'profile_links': profile_links
        }

        contact_info = get_contact_info(linkedin_parameters)
        
        # bot.login()
        # bot.security_check()
        # bot.start_applying()
        
        print(company_name)
        return redirect(url_for("index", result="okay"))
    result = request.args.get("result")
    return render_template("home.html", result=result)


def init_browser():
    browser_options = Options()
    options = ['--disable-blink-features', '--no-sandbox', '--start-maximized', '--disable-extensions',
               '--ignore-certificate-errors', '--disable-blink-features=AutomationControlled', '--remote-debugging-port=9222']

    for option in options:
        browser_options.add_argument(option)
        
    browser_options.add_argument("--window-size=1920,1080")
    browser_options.add_argument('--disable-application-cache')
    browser_options.add_argument('--disable-gpu')
    browser_options.add_argument("--disable-popup-blocking")
    browser_options.add_argument("--profile-directory=Default")
    browser_options.add_argument("--disable-plugins-discovery")
    browser_options.add_argument("--incognito")
    browser_options.add_argument("user_agent=DN")
    browser_options.add_argument('--headless=new')
    browser_options.binary_location = binary_location
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=browser_options)

    driver.set_window_position(0, 0)
    driver.maximize_window()

    return driver

def get_profile_links(parameters):
    browser = init_browser()
    google_scrapper = GoogleScrapper(parameters, browser)
    profile_links = google_scrapper.get_profile_links()
    profile_links.pop(-1)
    return profile_links
        
def get_contact_info(parameters):
    browser = init_browser()
    linkedin_scrapper =  LinkedinEasyApply(parameters, browser)

    linkedin_scrapper.login()
    linkedin_scrapper.security_check()
    contact_info = linkedin_scrapper.get_contact_info()
    return contact_info

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    