# Imports for Selenium tester
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Locations
departing = ""
departing_state = ""
departing_country = ""

arriving = ""
arriving_state = ""
arriving_country = ""

# Airport 
departing_code = ""
arriving_code = ""

# Dates
start_month = ""
start_day = ""
start_year = ""

end_month = ""
end_day = ""
end_year = ""


# Selenium path
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def main():   
    """
    Operates the main txt file
    """
    with open(arriving+'_tickets.txt', 'w') as f:
        f.write(arriving+"\n\n")

        f.write("Expedia\n")
        expedia(f)
        
        f.write("Kayak\n")
        kayak(f)

        f.write("Kiwi\n")
        kiwi(f)

        f.write("Student Universe\n")
        student_universe(f)


def expedia(f): 
    """Goes through the expedia search bar and lowest price"""

    # Search link
    name1 = departing.replace(" ", "%20")
    name2 = arriving.replace(" ", "%20")
    link = "https://www.expedia.com/Flights-Search?leg1=from%3A"+name1+"%20%28"+departing_code+"%20-%20All%20Airports%29%2Cto%3A"+name2+"%20%28"+arriving_code+"-All%20Airports%29%2Cdeparture%3A"+start_month+"%2F"+start_day+"%2F"+start_year+"TANYT&leg2=from%3A"+name2+"%20%28"+arriving_code+"-All%20Airports%29%2Cto%3A"+name1+"%20%28"+departing_code+"%20-%20All%20Airports%29%2Cdeparture%3A"+end_month+"%2F"+end_day+"%2F"+end_year+"TANYT&mode=search&options=carrier%3A%2A%2Ccabinclass%3A%2Cmaxhops%3A1%2Cnopenalty%3AN&pageId=0&passengers=adults%3A1%2Cchildren%3A0%2Cinfantinlap%3AN&trip=roundtrip "
    driver.get(link)

    # Get Price
    element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[contains(@class, "uitk-lockup-price")]')))
    f.write(element.text+"\n")
    f.write("Link:\n"+link+"\n\n")

def kayak(f):
    """Goes through the kayak search bar and finds lowest price"""

    # Search Link
    link = "https://www.kayak.com/flights/"+departing_code+"-"+arriving_code+"/"+start_year+"-"+start_month+"-"+start_day+"/"+end_year+"-"+end_month+"-"+end_day+"?sort=price_a"
    driver.get(link)

    # Get Price
    time.sleep(15)
    element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@class, "price option-text")]')))
    f.write(element.text+"\n")
    f.write("Link:\n"+link+"\n\n")

def kiwi(f):
    """Goes through the Kiwi website and finds lowest price"""

    # Search link
    state = departing_state
    if state!="":
        state = state+"-"
    departing_location = (departing+"-"+state+departing_country).replace(" ", "-")
    state = arriving_state
    if state!="":
        state = state+"-"
    arriving_location = (arriving+"-"+state+arriving_country).replace(" ", "-")

    link = 'https://www.kiwi.com/en/search/results/'+departing_location+'/'+arriving_location+'/2023-06-01/2023-06-23?sortBy=price'
    driver.get(link)

    # Get Price
    element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[contains(@data-test, "ResultCardPrice")]')))
    f.write(element.text+"\n")
    f.write("Link:\n"+link+"\n\n")

def student_universe(f):
    """Goes through the student universe website and finds the lowest price"""

    # Search Link
    link = "https://www.studentuniverse.com/flights/1/"+departing_code+"/"+arriving_code+"/"+start_year+"-"+start_month+"-"+start_day+"/"+arriving_code+"/"+departing_code+"/"+end_year+"-"+end_month+"-"+end_day+"?flexible=true&premiumCabins=false&source=productHome"
    driver.get(link)

    # Get Price
    element = WebDriverWait(driver, 150).until(EC.element_to_be_clickable((By.XPATH,'//*[contains(@uib-tooltip, "Cheapest")]')))
    f.write(element.text+"\n")
    f.write("Link:\n"+link+"\n\n")

main()
