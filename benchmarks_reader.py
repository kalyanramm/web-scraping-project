from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time

csv_file = open('benchmarks.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

driver = webdriver.Chrome()
driver.get("https://www.cpubenchmark.net/CPU_mega_page.html")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cputable"]/tbody/tr[1]/td[2]')))

columns_button = driver.find_element_by_xpath('//*[@id="main_content"]/div[3]/div[2]/div[1]/label')
columns_button.click()

auto_button = driver.find_element_by_xpath('//*[@id="columnSelector"]/label[1]/input')
auto_button.click()

price_button = driver.find_element_by_xpath('//*[@id="columnSelector"]/label[2]/input')
price_button.click()

cpu_value_button = driver.find_element_by_xpath('//*[@id="columnSelector"]/label[3]/input')
cpu_value_button.click()

thread_value_button = driver.find_element_by_xpath('//*[@id="columnSelector"]/label[5]/input')
thread_value_button.click()

power_perf_button = driver.find_element_by_xpath('//*[@id="columnSelector"]/label[7]/input')
power_perf_button.click()

test_date_button = driver.find_element_by_xpath('//*[@id="columnSelector"]/label[8]/input')
test_date_button.click()

columns_button = driver.find_element_by_xpath('//*[@id="main_content"]/div[3]/div[2]/div[1]/label')
columns_button.click()

show_entries_button = driver.find_element_by_xpath('//*[@id="cputable_length"]/label/select')
show_entries_button.click()

all_entries_button = driver.find_element_by_xpath('//*[@id="cputable_length"]/label/select/option[4]')
all_entries_button.click()

table_id = driver.find_element_by_xpath('//*[@id="cputable"]/tbody')
rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table

index = 1
for row in rows:
    review_dict = {}

    row_elements = row.find_elements(By.TAG_NAME, "td")
    review_dict['cpu_name'] = row_elements[1].text
    review_dict['price'] = row_elements[2].text
    review_dict['cpu_mark'] = row_elements[3].text
    review_dict['cpu_value'] = row_elements[4].text
    review_dict['thread_mark'] = row_elements[5].text
    review_dict['thread_value'] = row_elements[6].text
    review_dict['tdp_w'] = row_elements[7].text
    review_dict['power_perf'] = row_elements[8].text
    review_dict['test_date'] = row_elements[9].text
    review_dict['socket'] = row_elements[10].text
    review_dict['category'] = row_elements[11].text

    details_control_button = row_elements[0]
    details_control_button.click()

    element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cputable"]/tbody/tr[{0}]/td/div/div[1]/span'.format(index+1))))
    childRow = table_id.find_element_by_xpath('//*[@id="cputable"]/tbody/tr[{0}]'.format(index+1))
    
    review_dict['clock_speed'] = childRow.find_element_by_xpath('//*[@id="cputable"]/tbody/tr[{0}]/td/div/div[1]'.format(index+1)).text
    review_dict['turbo_speed'] = childRow.find_element_by_xpath('//*[@id="cputable"]/tbody/tr[{0}]/td/div/div[2]'.format(index+1)).text
    review_dict['cores_threads'] = childRow.find_element_by_xpath('//*[@id="cputable"]/tbody/tr[{0}]/td/div/div[3]'.format(index+1)).text
    review_dict['rank'] = childRow.find_element_by_xpath('//*[@id="cputable"]/tbody/tr[{0}]/td/div/div[4]'.format(index+1)).text
    review_dict['samples'] = childRow.find_element_by_xpath('//*[@id="cputable"]/tbody/tr[{0}]/td/div/div[5]'.format(index+1)).text

    details_control_button.click()
    writer.writerow(review_dict.values())
    print(review_dict.values())
    index+=1

csv_file.close()
driver.close()