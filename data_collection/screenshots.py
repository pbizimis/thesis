import csv
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from predict_good_or_cookie import make_prediction
import os
import shutil

line_count = 1
start_at = 50476

output_path_good = "/mnt/d/new_images/good"
output_path_bad = "/mnt/d/new_images/bad"
output_path_temp = "/mnt/d/new_images/temp_before_prediction"
output_path_screenshot = "/mnt/d/new_images/screenshots/"

def get_most_used_color_percentage(im):
    image_dict = {}

    for pixel in im.getdata():
        try:
            image_dict[pixel] += 1
        except:
            image_dict[pixel] = 1

        
    max_key = max(image_dict, key=lambda key: image_dict[key])

    highest_percentage = image_dict[max_key] / 4194304

    return highest_percentage

def downsample_image(im):
    out = im.convert("RGB")
    out = out.resize((512,512),Image.ANTIALIAS)
    return out


with open('tranco_GW9K.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    while line_count < 100000:

        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=2064,2180")
        service = Service('/usr/bin/chromedriver.exe')
        service.start()
        driver = webdriver.Remote(service.service_url, options=chrome_options)

        for row in csv_reader:
            # find start_at website
            if line_count < start_at:
                line_count += 1
                continue

            # break loop to open new driver (close and start up chrome)
            if line_count % 300 == 0:
                break

            # build path
            domain_str = str(row[1])
            domain_file_name = domain_str.replace(".","_")+".png"

            # final dataset folder
            domain_output_path_good = os.path.join(output_path_good, domain_file_name)
            # outsourced images (for control)
            domain_output_path_bad = os.path.join(output_path_bad, domain_file_name)
            # temporary image files for downsampling 512x512
            domain_output_path_temp = os.path.join(output_path_temp, domain_file_name)
            # inital screenshots 2048x2048
            domain_output_path_screenshot = os.path.join(output_path_screenshot, domain_file_name)

            try:
                # set timeout 4s
                driver.set_page_load_timeout(4)
                # get page
                driver.get("https://" + domain_str)

                driver.save_screenshot(domain_output_path_screenshot)

                im = Image.open(domain_output_path_screenshot)

                # check if image has a dominant color with over 85%
                percentage = get_most_used_color_percentage(im)
                if percentage > 0.85:
                    im.save(domain_output_path_bad)
                    continue

                # check if the trained ai predicts a cookie screenshot
                downsampled_image = downsample_image(im)
                downsampled_image.save(domain_output_path_temp)

                prediction = make_prediction(domain_output_path_temp)

                if prediction == 0:
                    shutil.move(domain_output_path_temp, domain_output_path_good)
                elif prediction == 1:
                    shutil.move(domain_output_path_temp, domain_output_path_bad)
            except:
                print(line_count, "FAILED")

            line_count+=1
        
        line_count+=1
        try:
            driver.close()
        except:
            print("Could not close window.")
