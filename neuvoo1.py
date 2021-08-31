from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(executable_path="/home/praveena/Downloads/chromedriver")
driver.maximize_window()
dataframe = pd.DataFrame(columns=["Title", "Description"])

for i in range(0, 10, 10):

    driver.get("https://neuvoo.ca/jobs/?k=machine+learning&l=North+York%2C+Ontario&f=&o=&p=&r=15=" + str(i))
    driver.implicitly_wait(5)

    all_jobs = driver.find_elements_by_class_name('card__job-c')

    for job in all_jobs:

        result_html = job.get_attribute('innerHTML')
        soup = BeautifulSoup(result_html, 'html.parser')

        try:
            title = soup.find("a", class_="card__job-link").text.replace('\n', '')
        except:
            title = 'None'

        try:
            description = soup.find(class_="card__job-snippet").text
        except:
            description = 'None'

        # try:
        #     company = soup.find(class_="link").text.replace("\n", "").strip()
        # except:
        #     company = 'None'

        # try:
        #     salary = soup.find(class_="salary").text.replace("\n", "").strip()
        # except:
        #     salary = 'None'

        # sum_div = job.find_elements_by_class_name("summary")[0]
        # try:
        #     sum_div.click()
        # except:
        #     close_button = driver.find_elements_by_class_name("popover-x-button-close")[0]
        #     close_button.click()
        #     sum_div.click()
        # try:
        #     jd = driver.find_element_by_css_selector('card').text
        #     #print(jd)
        # except:
        #     jd = 'None'

        dataframe = dataframe.append({'Title': title,
                                      'Description': description,
                                     },
                                     ignore_index=True)

dataframe.to_csv("ml1.csv", index=False)