import pandas as pd

def sentiment_analysis_model(name):
    import selenium 
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from time import sleep
    import getpass

    my_user = "enter your user id"
    my_pass = "enter your password"


    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    # Create the Chrome driver with options
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)


    # # Simply create the Chrome driver without specifying the path
    # driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    # Now you can use the driver for your web automation tasks
    driver.get("https://x.com/i/flow/login")


    user_id = driver.find_element(By.XPATH,"//input[@type='text']")
    user_id.send_keys(my_user)
    user_id.send_keys(Keys.ENTER)
    # driver.implicitly_wait(10)

    # my_mob = "enter your mobile number"
    # mob_no = driver.find_element(By.XPATH,"//input[@type='text']")
    # mob_no.send_keys(my_mob)
    # mob_no.send_keys(Keys.ENTER)
    # driver.implicitly_wait(10)
    try:
        mob_no = driver.find_element(By.XPATH, "//input[@type='text']")
        my_mob = "8875316737"  # Replace with your phone number if needed
        mob_no.send_keys(my_mob)
        mob_no.send_keys(Keys.ENTER)
    except:
        print("No phone number step required")
    password = driver.find_element(By.XPATH,"//input[@type='password']")
    password.send_keys(my_pass)
    password.send_keys(Keys.ENTER)

    # name = input('What is your name?\n')  
    search_item = name
    # search_item = "Narendra Modi"
    search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
    search_box.send_keys(search_item)
    search_box.send_keys(Keys.ENTER)

    print("Checkpoint: Section 1 completed")

    all_tweets = set()

    tweets = driver.find_elements(By.XPATH,"//div[@data-testid='tweetText']")
    while True:
        for tweet in tweets:
            all_tweets.add(tweet.text)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(3)
        tweets = driver.find_elements(By.XPATH,"//div[@data-testid='tweetText']")
        if len(all_tweets)>100:
            break

    print("Checkpoint: Section 2 completed")

    all_tweets = list(all_tweets)
    all_tweets[0]


    # Cleaning the tweets


    import pandas as pd
    pd.options.display.max_colwidth = 1000
    import re
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    stp_words = stopwords.words('english')
    # stp_words
    # stop_words_hi = stopwords.words('hindi')
    # stop_words_hi

    df = pd.DataFrame(all_tweets,columns=['tweets'])
    # df.head()

    from deep_translator import GoogleTranslator
    import pandas as pd

    # Assuming you have a DataFrame 'df' with a column 'tweets'
    # Create a new column 'english_tweets' to store the translations
    df['english_tweets'] = df['tweets'].apply(lambda sentence: GoogleTranslator(source='auto', target='en').translate(sentence))
    print("Checkpoint: Section 3 completed")

    # Now 'df' contains both the original tweets and their English translations
    # print(df[['tweets', 'english_tweets']])


    one_tweet =  df['tweets']
    one_tweet

    # !pip install textblob
    from textblob import TextBlob
    from wordcloud import WordCloud

    def TweetCleaning(tweet):
        clean_tweet = re.sub('[^a-zA-Z0-9]',' ',tweet)
        clean_tweet = ' '.join(word for word in clean_tweet.split() if word not in stp_words)
        return clean_tweet

    def calPolarity(tweet):
        return TextBlob(tweet).sentiment.polarity

    def calSubjectivity(tweet):
        return TextBlob(tweet).sentiment.subjectivity

    def segmentation(tweet):
        if tweet >0:
            return "positive"
        if tweet==0:
            return "neutral"
        else:
            return "negative"

    # clean_tweet

    # clean_tweet.split()

    # type(clean_tweet)

    df['Cleaned_tweets'] = df['english_tweets'].apply(TweetCleaning)
    # df.head(20)

    print("Checkpoint: Section 4 completed")

    # df.shape

    df['tPolarity'] = df['Cleaned_tweets'].apply(calPolarity)
    df['tSubjectivity'] = df['Cleaned_tweets'].apply(calSubjectivity)
    df['segmentation'] = df['tPolarity'].apply(segmentation)
    # df.head()
    sentiment_counts = df['segmentation'].value_counts().reset_index()
    sentiment_counts.columns = ['segmentation', 'count']
    return sentiment_counts

