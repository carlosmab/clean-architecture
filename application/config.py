import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig:
    """Base config"""
    

class ProductionConfig(DefaultConfig):
    """Production config"""
    pass

class DevelopmentConfig(DefaultConfig):
    """Development config"""
    pass
    
    
class TestingConfig(DefaultConfig):
    """Test config"""
    pass
    TESTING = True