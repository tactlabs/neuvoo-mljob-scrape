from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(executable_path="/home/praveena/Downloads/chromedriver")
driver.maximize_window()
dataframe = pd.DataFrame(columns=["Title", "Location", "Company", "Salary", "Description"])

for i in range(0, 10, 10):

    driver.get("https://www.indeed.com/jobs?q=Senior+Software+Engineer&l=Philadelphia%2C+PA&start=" + str(i))
    driver.implicitly_wait(5)

    all_jobs = driver.find_elements_by_class_name('result')

    for job in all_jobs:

        result_html = job.get_attribute('innerHTML')
        soup = BeautifulSoup(result_html, 'html.parser')

        try:
            title = soup.find("a", class_="jobtitle").text.replace('\n', '')
        except:
            title = 'None'

        try:
            location = soup.find(class_="location").text
        except:
            location = 'None'

        try:
            company = soup.find(class_="companyLocation").text.replace("\n", "").strip()
        except:
            company = 'None'

        try:
            salary = soup.find(class_="salary").text.replace("\n", "").strip()
        except:
            salary = 'None'

        # sum_div = job.find_elements_by_class_name("summary")[0]
        # try:
        #     sum_div.click()
        # except:
        #     close_button = driver.find_elements_by_class_name("popover-x-button-close")[0]
        #     close_button.click()
        #     sum_div.click()
        try:
            jd = driver.find_element_by_css_selector('div#vjs-desc').text
            #print(jd)
        except:
            jd = 'None'

        dataframe = dataframe.append({'Title': title,
                                      'Location': location,
                                      "Company": company,
                                      "Salary": salary,
                                      "Description": jd},
                                     ignore_index=True)

dataframe.to_csv("c.csv", index=False)