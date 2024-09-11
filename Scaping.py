from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
import os
from urllib.parse import urlparse

driver = webdriver.Chrome()

url = "https://www.misti.gov.kh/documents?type=law"

driver.get(url)

ng_content = driver.find_element(By.XPATH, '/html/body/app-root/app-documents/app-base-page-layout/div/div[2]/div[2]')

print(ng_content)

box = ng_content.find_element(By.TAG_NAME, 'div')
print(box)
boxs = box.find_elements(By.TAG_NAME, 'app-document-card')
print(boxs)




for b in boxs:
    near_link = b.find_element(By.XPATH, '/html/body/app-root/app-documents/app-base-page-layout/div/div[2]/div[2]/div/app-document-card[1]/div/div[2]/div[2]')
    print(near_link)
    pdf_url = near_link.find_element(By.TAG_NAME, 'a').get_attribute('href')
    
# Parse the URL to get the filename
filename = os.path.basename(urlparse(pdf_url).path)

# The file path where you want to save the PDF
save_path = os.path.join("D:/Help/Downloads", filename)

# Download the PDF file
response = requests.get(pdf_url)

# Write the content of the response (PDF data) to a file
with open(save_path, 'wb') as pdf_file:
    pdf_file.write(response.content)

print(f"PDF downloaded successfully and saved as {filename}")


time.sleep(15)
