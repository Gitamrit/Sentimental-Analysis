from flask import Flask, request, render_template
import pandas as pd
import plotly.express as px
import requests
from bs4 import BeautifulSoup
import urllib.parse
from your_script import sentiment_analysis_model  # import your sentiment analysis function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']
        
        # Fetch sentiment analysis
        df1 = sentiment_analysis_model(name1)
        df2 = sentiment_analysis_model(name2)
        
        # Fetch images
        img_url1 = fetch_wikipedia_image(name1)
        img_url2 = fetch_wikipedia_image(name2)
        
        # Create plot
        fig = create_plot(df1, df2, name1, name2)
        graphJSON = fig.to_json()
        
        return render_template('index.html', graphJSON=graphJSON, img_url1=img_url1, img_url2=img_url2)
    
    return render_template('index.html', graphJSON=None, img_url1=None, img_url2=None)

def fetch_wikipedia_image(query):
    # Normalize query to replace spaces with underscores
    query = query.replace(' ', '_')
    base_url = f"https://en.wikipedia.org/wiki/{query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            image_url = None

            # Find the first image in the infobox (common place for lead images in Wikipedia)
            infobox = soup.find('table', {'class': 'infobox'})
            if infobox:
                image_tag = infobox.find('img')
                if image_tag:
                    image_url = image_tag.get('src')
                    # Handle relative URLs
                    if image_url and not image_url.startswith('http'):
                        image_url = urllib.parse.urljoin(base_url, image_url)

            return image_url
        else:
            print(f"Failed to fetch Wikipedia page: Status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Wikipedia page: {str(e)}")
        return None

def create_plot(df1, df2, name1, name2):
    df1['name'] = name1
    df2['name'] = name2
    combined_df = pd.concat([df1, df2])
    fig = px.bar(combined_df, x='segmentation', y='count', color='name', barmode='group', title="Sentiment Analysis")
    return fig

if __name__ == '__main__':
    app.run(debug=True)
