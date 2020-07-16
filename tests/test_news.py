import unittest
from app.models import News

class NewsTest(unittest.TestCase):
   
    def setUp(self):
        
        self.new_news = News(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

    