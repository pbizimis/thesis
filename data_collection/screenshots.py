import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

line_count = 1
start_at = 26286

with open('tranco_GW9K.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    while line_count < 50000:
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=2064,2180")
        service = Service('/usr/bin/chromedriver.exe')
        service.start()
        driver = webdriver.Remote(service.service_url, options=chrome_options)


        for row in csv_reader:
            if line_count < start_at:
                line_count += 1
                continue

            if line_count % 300 == 0:
                break

            domain_str = str(row[1])
            try:
                driver.set_page_load_timeout(4)
                driver.get("https://" + domain_str)
                driver.save_screenshot("/mnt/d/ScreenshotsThesis6/"+domain_str.replace(".","_")+".png")
            except:
                print(line_count, "FAILED")

            line_count+=1
        
        line_count+=1
        try:
            driver.close()
        except:
            print("Could not close window.")