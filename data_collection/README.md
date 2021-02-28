# Data Collection

This script uses Python 3.6 and Selenium 3.141 to collect screenshots of popular websites. I use the Tranco list generated on 15 February 2021 (https://tranco-list.eu/list/GW9K).

Screenshot resolution is 2048x2048. In the script, the numbers are different because of browser borders (chrome-driver). A headless window should not be used because many websites block those requests.

Every 300 websites, the browser will be closed and reopened. This helped to keep the script running for long periods of time.

```
python -m pip install -U pip (21.0.1)
pip install selenium
pip install google-cloud-aiplatform
```

Pipeline explanation:
- define output folder paths
- init chrome webdriver
- traverse csv
- every 300 websites, close driver and open a new window
- open website
- if website has a dominant color with over 85%, image is probably "bad" (go next)
- use AutoML ai (trained on cookie images) to predict if image contains cookie windows or not
- if both tests are successfull, save image
- next website