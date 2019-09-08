from app import app
import urllib.request,json
from .models import news
# from news import News

# Getting api key
apiKey = app.config['NEWS_API_KEY']

# getting the movie base url

base_url = app.config["NEWS_API_BASE_URL"]


# .........................get news section............................

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    
    get_news_url = base_url.format(category,apiKey)
    

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response["sources"]:
            news_results_list = get_news_response["sources"]
            news_results = process_results(news_results_list)

    return news_results




def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id') 
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        
        # news_object = news(id,name,description,url,category,country,language)
        # news_results.append(news_object)

    return news_results


    # ..........................end of get news...................................

def get_articles(id):
    '''
    function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = articles_url.format(id,apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
    articles_results = json.loads(url.read())

    articles_object = None
    if articles_results['articles']:
        articles_object = process_articles(articles_results['articles'])

	return articles_object


























































