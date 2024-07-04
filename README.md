# Sentiment Analysis Web Application
The Sentiment Analysis Web Application is designed to analyze tweets related to two public figures. Here are its key features:

+ Sentiment Analysis:
  + The application performs sentiment analysis on the top 100 tweets associated with the specified names.
  + It categorizes tweets as positive, negative, or neutral based on their content.
+ Visualization:
  + The sentiment results are visualized using a bar chart, providing an overview of the overall sentiment distribution.
  + Users can quickly grasp the sentiment trends related to the given names.
+ Wikipedia Image Retrieval:
  + The application fetches images from Wikipedia for the specified names.
  + These images enhance the user experience and provide context.
+ Multilingual Support:
  + The application supports analyzing tweets in all languages.
  + Users can explore sentiment across diverse linguistic contexts.






![WhatsApp Image 2024-07-02 at 11 01 21_651844e4](https://github.com/Gitamrit/Sentimental-Analysis/assets/163405281/ac1ef2c4-0603-4dbd-a013-e559f40bf0a8)


## Technologies Used
Python,
Flask,
Selenium,
Plotly,
BeautifulSoup,
Requests,
TextBlob,
HTML/CSS
## How to use
Since the website is not hosted yet , you need to do it manually by hosting it locally . Clone the Github link and run python app.py on your terminal.


## Handling Selenium Errors and Timeouts in Web Scraping:

### “Frame Not Found” Error:
+ When encountering a “frame not found” error in Selenium, it typically occurs due to issues with interacting with iframes (inline frames) on a web page.
+ To resolve this:
  + Run your script in non-headless mode (i.e., with a visible browser window).
  + Observe which pages or elements are popping up during the login process.
  + Inspect the page source to identify iframes and ensure proper interaction with them.
### Google Translate Timeout Error:
+ If you encounter a timeout error while using Google Translate API:
  + Retry the translation request after waiting for a few minutes. Sometimes, temporary server issues can cause timeouts.
  + Alternatively, consider obtaining a Google API key. This key can increase your API quota and provide more reliable access to the translation service.


