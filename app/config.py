class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL ="https://newsapi.org/v2/sources?language=en&category={}&apiKey={}"

        # NEWS_API_BASE_URL ="http://newsapi.org/v2/everything?q=business&from=2019-08-07&sortBy=publishedAt&apiKey={}"
        
    pass




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True