from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from links import cdc_website
from links import google
from links import PATH
import time
from tkinter import *

driver = webdriver.Chrome(PATH)

class covidProj:

    def __init__(self, root):
        self.driver = driver
        self.google = google
        self.master = root
        self.cdc = cdc_website

        #covid case tracker title, label, entry and button
        self.master.title('Covid-19 Case Tracker')
        US_Covid_Count = self.US_Covid_Count = Label(self.master, text = 'Covid-19 Case Tracker',bg='#F5F5F5')
        self.US_Covid_Count.config(font =("Lucida Grande",30))
        US_Covid_Count.place(x =250, y = 0)

        #total numbers determines the total overall covid cases + deaths
        overallCovidNumbers = self.overallCovidNumbers = Label(self.master, text = ' Hit Yes To See US Total Covid Cases & Deaths', bg='#F5F5F5')
        self.overallCovidNumbers.config(font =("Lucida Grande",14))
        overallCovidNumbers.place(x =0, y = 50)
        overall_US_Case_Button = self.overall_US_Case_Button = Button(self.master, text='Yes', command = self.US_Case_Tracker, bg='#0000FF', fg='blue',width = 10)
        overall_US_Case_Button.place(x = 325, y = 50)


        searchLabel = Label(master=root, text='Search for state',bg='#F5F5F5')
        searchLabel.place(x=0, y=100)
        self.stateEntry = Entry(self.master)
        self.stateEntry.place(x = 120, y = 100)
        searchButton = self.searchButton = Button(self.master, text='Enter', command = self.search_by_state, bg='#0000FF', fg='blue',width = 10)
        self.searchButton.config(font =("Lucida Grande",12))
        searchButton.place(x = 325, y = 105)

        #Num of cases label and entry
        state_results_label = self.state_results_label = Label(master=root, text='Number of Cases ',bg='#F5F5F5')
        self.state_results_label.config(font =("Lucida Grande",12))
        state_results_label.place(x = 0, y =150)
        self.state_case_count_Entry = Entry(self.master)
        self.state_case_count_Entry.place(x = 120,y = 150 )

        # Num of deaths label and entry
        state_deaths_label = self.state_deaths_label = Label(master=root, text='Number of Deaths ',bg='#F5F5F5' )
        self.state_deaths_label.config(font =("Lucida Grande",12))
        state_deaths_label.place(x = 325, y =150)
        self.state_death_count_Entry = Entry(self.master)
        self.state_death_count_Entry.place(x = 455, y = 150)

        # daily cases label and entry
        state_daily_cases = self.state_daily_cases = Label(master=root, text='Daily Cases ',bg='#F5F5F5' )
        self.state_daily_cases.config(font =("Lucida Grande",12))

        state_daily_cases.place(x = 0, y = 200)
        self.state_daily_cases_Entry = Entry(self.master)
        self.state_daily_cases_Entry.place(x = 120, y = 200)

        #num of daily cases label and entry
        state_daily_deaths =self.state_daily_deaths = Label(master=root, text='Daily Deaths ',bg='#F5F5F5' )
        self.state_daily_deaths.config(font =("Lucida Grande",12))
        state_daily_deaths.place(x = 325, y = 200)
        self.state_daily_deaths_Entry = Entry(self.master)
        self.state_daily_deaths_Entry.place(x = 455, y =200)

    def US_Case_Tracker(self):
        #clearing out Entries
        self.driver.get(self.cdc)
        self.state_case_count_Entry.delete(0, 'end')
        self.state_death_count_Entry.delete(0, 'end')
        self.state_daily_cases_Entry.delete(0, 'end')
        self.state_daily_deaths_Entry.delete(0, 'end')
        #selenium webscraping
        total_cases = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='card-number']")))
        total_deaths = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='viz002_usdeaths']/div/div[1]")))
        daily_cases = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='card-recent']")))
        daily_deaths = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='viz002_usdeaths']/div/div[2]")))

        #inserting info to the entries
        self.state_case_count_Entry.insert(0, total_cases.text)
        self.state_death_count_Entry.insert(0, total_deaths.text)
        self.state_daily_cases_Entry.insert(0, daily_cases.text)
        self.state_daily_deaths_Entry.insert(0, daily_deaths.text)
# ------------------------------------------------------------------------------------------------------------------------------------------
    def search_by_state(self):
        # clearing out Entries
        self.state_case_count_Entry.delete(0, 'end')
        self.state_death_count_Entry.delete(0, 'end')
        self.state_daily_cases_Entry.delete(0, 'end')
        self.state_daily_deaths_Entry.delete(0, 'end')
        #website for webscraping
        self.driver.get(self.google)
        #parsing html on google
        searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@type='text']")))
        state = self.stateEntry.get()
        state.title()
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

        #inserting variables to entries
        self.state_case_count_Entry.insert(0, state_cases.text)
        self.state_death_count_Entry.insert(0,state_deaths.text)
        self.state_daily_cases_Entry.insert(0, daily_case_count.text)
        self.state_daily_deaths_Entry.insert(0, daily_death_count.text)

if __name__ == '__main__':

    myTk = Tk()
    myTk.geometry('800x800')
    myTk.config(bg='#F5F5F5')
    my_gui = covidProj(myTk)
    myTk.mainloop()
