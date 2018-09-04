from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from fileo.testing_models import CreateTestModels
from search.search import SearchCycles


## TEST SEARCH APP CLASSES ##
class TestSearchApp(TestCase):
    
    def setUp(self):
       # self.request = 
        self.models = CreateTestModels()
        self.job = self.models.create_job()
        self.cycle = self.models.create_cycle()

    #def test