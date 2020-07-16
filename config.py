import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources=%s&apiKey=f0ca0d322bd94d3f909cddde43099b2b'
    NEWS_API_KEY = os.environ.get('f0ca0d322bd94d3f909cddde43099b2b')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

