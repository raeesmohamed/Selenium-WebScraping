import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from IPython.display import Image
import datetime

driver_service = Service(executable_path="C:\program files\chromedriver")
driver = webdriver.Chrome(service=driver_service)
driver.get('https://www.thetvdb.com/series/the-ellen-degeneres-show')

# //*[@id="tab-official"]/ul/li[3]/h4/a
# //*[@id="tab-official"]/ul/li[20]/h4/a

Date = []
Season_ep = []
Guests = []

for i in range(3,21):
    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                '//*[@id="tab-official"]/ul/li['+str(i)+']/h4/a')))
    element.click()
    
    for j in range(1,200):
        try:
            Season_ep.append(driver.find_element(By.XPATH,'//*[@id="page-season"]/div[5]/div[2]/div[1]/table/tbody/tr['+str(j)+']/td[1]').text)
            Guests.append(driver.find_element(By.XPATH,'//*[@id="page-season"]/div[5]/div[2]/div[1]/table/tbody/tr['+str(j)+']/td[2]/a').text)
            Date.append(driver.find_element(By.XPATH,'//*[@id="page-season"]/div[5]/div[2]/div[1]/table/tbody/tr['+str(j)+']/td[3]/div').text)
        except NoSuchElementException:
            continue
    print('Season: '+str(i-2)+'done')
#     //*[@id="page-season"]/div[5]/div[2]/div[1]/table/tbody/tr[1]/td[1]
#     //*[@id="page-season"]/div[5]/div[2]/div[1]/table/tbody/tr[1]/td[2]/a
#     //*[@id="page-season"]/div[5]/div[2]/div[1]/table/tbody/tr[1]/td[3]/div
    
#     //*[@id="page-season"]/div[5]/div[2]/div[1]/table/tbody/tr[166]/td[1]
#     //*[@id="page-season"]/div[5]/div[2]/div[1]/table/tbody/tr[166]/td[2]/a
#     //*[@id="page-season"]/div[5]/div[2]/div[1]/table/tbody/tr[166]/td[3]/div
    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                '//*[@id="page-season"]/div[4]/div/a[3]')))
    element.click()

d = zip(Season_ep,Date,Guests)
mapped = list(d)
df = pd.DataFrame(mapped, columns =['Season', 'Date','Guests'])