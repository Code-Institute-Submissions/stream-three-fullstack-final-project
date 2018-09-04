from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from fileo.testing_models import CreateTestModels
from search.search import SearchCycles
from cyclestatus.models import CycleStatus


## TEST SEARCH APP CLASSES ##
class TestSearchApp(TestCase):
    
    def setUp(self):
        self.models = CreateTestModels()
        self.member = self.models.get_member()
        self.client = self.models.get_client()
        self.models.create_job()
        self.models.create_cycle()
        self.cycle = self.models.get_cycle()

        self.member_request = RequestFactory().get('/')
        self.member_request.user = self.member
        SessionMiddleware().process_request(self.member_request)
        self.member_request.session.save()

        self.client_request = RequestFactory().get('/')
        self.client_request.user = self.client
        SessionMiddleware().process_request(self.client_request)
        self.client_request.session.save()



    def test_filter_cycles_by_member(self):
        kwargs = {'search': 'testclient',
                    'order' : 'newest'}
        
        cycles = SearchCycles(self.member_request, **kwargs).filter_by_member()

        self.assertTrue(cycles)

    def test_filter_cycles_by_client(self):
        kwargs = {'search': 'testclient',
                'order' : 'newest'}
       
        cycles = SearchCycles(self.client_request, **kwargs).filter_by_client()

        self.assertTrue(cycles)

    def test_search_all_cycles_as_member(self):
        kwargs = {'search': 'testclient',
                'order' : 'newest'}
       
        cycles = SearchCycles(self.member_request, **kwargs).search_all_cycles()

        self.assertTrue(cycles)

    def test_search_all_cycles_as_client(self):
        kwargs = {'search': 'Test Cycle',
                'order' : 'newest'}
        
        cycles = SearchCycles(self.client_request, **kwargs).search_all_cycles()

        self.assertTrue(cycles)

    def test_search_pending_cycles_returns_false(self):
        kwargs = {'search': 'testclient',
                'order' : 'newest'}
       
        cycles = SearchCycles(self.member_request, **kwargs).search_pending_cycles()

        self.assertFalse(cycles)

    def test_search_pending_cycles_returns_true(self):
        kwargs = {'search': 'testclient',
                'order' : 'newest'}
       
        status = CycleStatus.objects.get(cycle=self.cycle)
        status.pending = True
        status.save(update_fields=['pending'])
       
        cycles = SearchCycles(self.member_request, **kwargs).search_pending_cycles()

        self.assertTrue(cycles)

    def test_search_cancelled_cycles_returns_false(self):
        kwargs = {'search': 'testclient',
                'order' : 'newest'}
       
        cycles = SearchCycles(self.member_request, **kwargs).search_cancelled_cycles()

        self.assertFalse(cycles)

    def test_search_cancelled_cycles_returns_true(self):
        kwargs = {'search': 'testclient',
                'order' : 'newest'}
       
        status = CycleStatus.objects.get(cycle=self.cycle)
        status.cancelled = True
        status.save(update_fields=['cancelled'])
        
        cycles = SearchCycles(self.member_request, **kwargs).search_cancelled_cycles()

        self.assertTrue(cycles)

    def test_search_completed_cycles_returns_false(self):
        kwargs = {'search': 'testclient',
                'order' : 'newest'}
      
        cycles = SearchCycles(self.member_request, **kwargs).search_completed_cycles()

        self.assertFalse(cycles)

    def test_search_completed_cycles_returns_true(self):
        kwargs = {'search': 'testclient',
                'order' : 'newest'}
       
        status = CycleStatus.objects.get(cycle=self.cycle)
        status.complete = True
        status.save(update_fields=['complete'])
       
        cycles = SearchCycles(self.member_request, **kwargs).search_completed_cycles()

        self.assertTrue(cycles)

    def test_search_active_cycles_returns_false(self):
        kwargs = {'search': 'testclient',
                'order' : 'newest'}
       
        status = CycleStatus.objects.get(cycle=self.cycle)
        status.complete = True
        status.cancelled = True
        status.pending = True
        status.save(update_fields=['complete',
                                    'cancelled',
                                    'pending'])

        cycles = SearchCycles(self.member_request, **kwargs).search_active_cycles()

        self.assertFalse(cycles)

    def test_search_active_cycles_returns_true(self):
        kwargs = {'search': 'testclient',
                'order' : 'newest'}
        
        cycles = SearchCycles(self.member_request, **kwargs).search_active_cycles()

        self.assertTrue(cycles)
