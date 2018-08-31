from django.test import TestCase
from managecycle import view_func
from fileo.test_models import CreateTestModels
from .forms import CycleForm

## TEST MANAGE CYCLE VIEW HELPER FUNCTIONS ##
class TestManageCycleViewFunc(TestCase):

    def setUp(self):
        self.models = CreateTestModels()
        self.member = self.models.get_member()
        self.job = self.models.create_job()
        self.new_form = CycleForm(self.member.pk, {'cycle_title':'new cycle',
                                        'description': 'new description',
                                        'location': 'new location',
                                        'start_date': '2019-01-01',
                                        'end_date': '2019-01-01',
                                        'jobs': self.job.pk})

    def test_create_cycle(self):
        new_form = self.new_form
        if new_form.is_valid():
            new_cycle = view_func.create_cycle(new_form, self.member)
            cycle = self.models.get_cycle()

        self.assertEqual('new cycle', cycle.cycle_title)
        self.assertTrue(new_cycle)

    def test_cycles_do_not_exist(self):
        empty_cycles = view_func.get_user_cycles(self.member)
        
        self.assertFalse(empty_cycles)

    def test_get_user_cycles(self):
        self.models.create_cycle()
        cycles = view_func.get_user_cycles(self.member)

        self.assertTrue(cycles)

    def test_update_cycle(self):
        self.models.create_cycle()
        cycle = self.models.get_cycle()
        title = cycle.cycle_title
        description = cycle.description
        location = cycle.location
        start = cycle.start_date
        end = cycle.end_date

        new_form = self.new_form
        if new_form.is_valid():
            update_cycle = view_func.update_cycle(cycle,new_form)
            updated_cycle = self.models.get_cycle()

        self.assertTrue(update_cycle)
        self.assertNotEqual(title, updated_cycle.cycle_title)
        self.assertNotEqual(description, updated_cycle.description)
        self.assertNotEqual(location, updated_cycle.location)
        self.assertNotEqual(start, updated_cycle.start_date)
        self.assertNotEqual(end, updated_cycle.end_date)

    def test_clear_status(self):
        self.models.create_cycle()
        cycle = self.models.get_cycle()
        self.models.create_cycle_status()
        status = self.models.get_cycle_status()
        status.approve_quote = True
        status.contest_quote = True
        status.approve_po = True
        status.contest_po = True
        status.approve_invoice = True
        status.contest_invoice = True
        status.complete = True
        status.pending = True
        status.cancelled = True
        status.save()

        reset = view_func.clear_status(cycle)

        self.assertTrue(reset)
        self.assertFalse(reset.approve_quote)
        self.assertFalse(reset.contest_quote)
        self.assertFalse(reset.approve_po)
        self.assertFalse(reset.contest_po)
        self.assertFalse(reset.approve_invoice)
        self.assertFalse(reset.contest_invoice)
        self.assertFalse(reset.complete)
        self.assertFalse(reset.pending)
        self.assertFalse(reset.cancelled)

    def test_clear_cycle_value(self):
        self.models.create_cycle()
        cycle = self.models.get_cycle()
        
        value = view_func.clear_value(cycle)
       
        self.assertEqual(str(value.cycle_value), '0.00 GBP')

        

