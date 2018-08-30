from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from search.search import SearchCycles
from fileo.test_models import CreateTestModels
from .view_func import get_searched_cycles, SetSessionValues

## TESTS FOR CYCLES APP VIEW HELPER FUNCTIONS/CLASSES ##
class TestCyclesViewFunctions(TestCase):
    
    def setUp(self):
        self.new_models = CreateTestModels()
        self.job = self.new_models.create_job()
        self.cycle = self.new_models.create_cycle()
        self.new_models.create_cycle_status()
        self.status = self.new_models.get_cycle_status()
        
    def test_get_all_searched_cycles(self):
        member = self.new_models.get_member()
        search = {'search': self.cycle.client,
                    'order': 'oldest',
                    'sort': 'all'}
        request = RequestFactory().get('/', search)
        request.user = member

        SessionMiddleware().process_request(request)
        request.session.save()

        cycles = get_searched_cycles(request)
        
        self.assertTrue(cycles)
        self.assertEqual(cycles[0].cycle.client, self.cycle.client)

    def test_get_all_pending_cycles(self):
        self.status.pending = True
        self.status.save(update_fields=['pending'])

        member = self.new_models.get_member()
        search = {'search': self.cycle.client,
                    'order': 'oldest',
                    'sort': 'pending'}
        request = RequestFactory().get('/', search)
        request.user = member

        SessionMiddleware().process_request(request)
        request.session.save()

        cycles = get_searched_cycles(request)

        self.assertTrue(cycles)
        self.assertEqual(cycles[0].cycle.client, self.cycle.client)

    def test_get_all_cancelled_cycles(self):
        self.status.cancelled = True
        self.status.save(update_fields=['cancelled'])

        member = self.new_models.get_member()
        search = {'search': self.cycle.client,
                    'order': 'oldest',
                    'sort': 'cancelled'}
        request = RequestFactory().get('/', search)
        request.user = member

        SessionMiddleware().process_request(request)
        request.session.save()

        cycles = get_searched_cycles(request)

        self.assertTrue(cycles)
        self.assertEqual(cycles[0].cycle.client, self.cycle.client)

    def test_get_all_active_cycles(self):
        ## ACTIVE CYCLES ARE CONSIDERED ACTIVE WHEN CANCELLED, PENDING, ##
        ## AND COMPLETE ARE SET TO FALSE ##
        member = self.new_models.get_member()
        search = {'search': self.cycle.client,
                    'order': 'oldest',
                    'sort': 'active'}
        request = RequestFactory().get('/', search)
        request.user = member

        SessionMiddleware().process_request(request)
        request.session.save()

        cycles = get_searched_cycles(request)

        self.assertTrue(cycles)
        self.assertEqual(cycles[0].cycle.client, self.cycle.client)

    def test_get_all_complete_cycles(self):
        self.status.complete = True
        self.status.save(update_fields=['complete'])

        member = self.new_models.get_member()
        search = {'search': self.cycle.client,
                    'order': 'oldest',
                    'sort': 'complete'}
        request = RequestFactory().get('/', search)
        request.user = member

        SessionMiddleware().process_request(request)
        request.session.save()

        cycles = get_searched_cycles(request)

        self.assertTrue(cycles)
        self.assertEqual(cycles[0].cycle.client, self.cycle.client)

        
    def test_filter_cycles_by_member(self):
        request = RequestFactory().get('/')
        request.user = self.new_models.get_member()
        SessionMiddleware().process_request(request)
        request.session.save()

        filter_by_member = SetSessionValues(request).filter_user()
       
        self.assertTrue(filter_by_member)
        self.assertEqual(filter_by_member[0].cycle.member, self.new_models.get_member())

    def test_filter_cycles_by_client(self):
        request = RequestFactory().get('/')
        request.user = self.new_models.get_client()
        SessionMiddleware().process_request(request)
        request.session.save()

        filter_by_client = SetSessionValues(request).filter_user()
       
        self.assertTrue(filter_by_client)
        self.assertEqual(filter_by_client[0].cycle.client, self.new_models.get_client())



