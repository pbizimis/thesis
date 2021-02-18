# Data Collection

This script uses Python 3.6 and Selenium 3.141 to collect screenshots of popular websites. I use the Tranco list generated on 15 February 2021 (https://tranco-list.eu/list/GW9K).

Screenshot resolution is 2048x2048. In the script, the numbers are different because of browser borders (chrome-driver). A headless window should not be used because many websites block those requests.

Every 300 websites, the browser will be closed and reopened. This helped to keep the script running for long periods of time.

```
pip install selenium
```
