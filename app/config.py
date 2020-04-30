class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass

class devConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True
    