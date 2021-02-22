from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from links import cdc_website
from links import google
from links import PATH
import time
from getpass import getpass

driver = webdriver.Chrome(PATH)
cdc_website = "https://covid.cdc.gov/covid-data-tracker/#cases_casesper100klast7days"
google = 'https://www.google.com/'

# cdc_website = "https://covid.cdc.gov/covid-data-tracker/#cases_casesper100klast7days"
# google = 'https://www.google.com/'
# driver.get(cdc_website)
def US_Case_Tracker(driver, website):
    driver.get(website)
    total_cases = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='card-number']")))
    total_deaths = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='viz002_usdeaths']/div/div[1]")))
    daily_cases = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='card-recent']")))
    daily_deaths = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='viz002_usdeaths']/div/div[2]")))
    print('Total Number of COVID-19 Cases: ', total_cases.text, ' and Total Number of Covid-19 Deaths: ',
          total_deaths.text)
    print('--------------------------------')
    print('Today We have: ', daily_cases.text, ' and ', daily_deaths.text, )
    """print('Total Number of COVID-19 Cases:',total_cases.text)
    daily_cases = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='card-recent']")))
    print('Today We have:', daily_cases.text)
    total_deaths = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='viz002_usdeaths']/div/div[1]")))
    print('Total Deaths:', total_deaths.text)
    daily_deaths = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='viz002_usdeaths']/div/div[2]")))
    print('Today We have', daily_deaths.text)
    """


# ------------------------------------------------------------------------------------------------------------------------------------------
def search_by_state(driver, google):
    driver.get(google)
    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@type='text']")))
    state = input('enter a state: ').title()
    searchbox.send_keys(state, ' covid cases')
    time.sleep(2)
    searchbox.send_keys(Keys.ENTER)
    state_cases = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='eTST2']/div[3]/div[1]/table/tbody/tr/td[1]/div[2]/div[1]/span")))
    state_deaths = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='eTST2']/div[3]/div[1]/table/tbody/tr/td[2]/div[2]/div[1]/span")))
    daily_case_count = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='eTST2']/div[3]/div[1]/table/tbody/tr/td[1]/div[3]/div/span")))
    daily_death_count = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='eTST2']/div[3]/div[1]/table/tbody/tr/td[2]/div[3]/div/span")))

    print('Covid-19 Numbers for', state)
    print('--------------------------------')
    print('Total Cases: ', state_cases.text, '  Total Deaths: ', state_deaths.text)
    print("Daily Cases: ", daily_case_count.text, " Daily Deaths:", daily_death_count.text)
    print('--------------------------------')


if __name__ == '__main__':
    US_Case_Tracker(driver, cdc_website)

    user_selection = input('would you like to search for a state to see their covid numbers? (Y/N) ')

    while (user_selection == 'y' or user_selection == 'Y'):
        search_by_state(driver, google)
        user_selection = input('would you like to search again? (Y/N)')
        if user_selection == 'N' or user_selection == 'n':
            print('goodbye')
            break


    """if(user_selection == 'y' or user_selection == 'Y' ):
        search_by_state(driver, google)

    search_again = input('would you like to search for another state?: (Y/N) ')
    if (search_again == 'y' or search_again == 'Y'):
        search_by_state(driver, google)
    else:
        print('goodbye')
        """

    """user = input('would you like to be updated on the latest covid cases & deaths?: (y or n)')
    if user == 'y' or user == 'Y':
        US_Case_Tracker(driver, cdc_website)

    else:
        user = input('would you like to search covid info on a state?: (Y or N)')
        if user == 'Y' or user == 'y':
            search_by_state(driver, google)
    """

"""
//*[@id="eTST2"]/div[3]/div[1]/table/tbody/tr/td[1]/div[3]/div/span
//*[@id="eTST2"]/div[3]/div[1]/table/tbody/tr/td[2]/div[2]/div[1]/span
#//*[@id="app"]/div/div[2]/section[4]/div[1]/div/a[1]
#//*[@id="svgviz005_uscases"]/g[1]/path[47] //*[@id="svgviz005_uscases"]/g[1]/path[51]
#//*[@id="svgviz005_uscases"]/g[1]/path[49]
#if __name__ == '__main__':
"""

