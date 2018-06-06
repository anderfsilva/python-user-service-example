import os

class Config(object):
    """
    Common configurations
    """

    DEBUG = False
    BUNDLE_ERRORS = True

    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 3000
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOST'),
        os.getenv('DB_PORT'),
        os.getenv('DB_NAME'))


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True

    SQLALCHEMY_ECHO = True


class StagingConfig(Config):
    """
    Staging configurations
    """

    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """


class TestingConfig(Config):
    """
    Testing configurations
    """

    DEBUG = True
    TESTING = True


app_config = {
    'dev': DevelopmentConfig,
    'sand': StagingConfig,
    'prod': ProductionConfig,
    'test': TestingConfig,
}
