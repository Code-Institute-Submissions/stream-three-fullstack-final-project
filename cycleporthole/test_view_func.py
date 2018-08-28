from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from fileo.test_models import CreateTestModels
from cycleporthole import view_func


## TEST PORTHOLE APP VIEW HELPER FUNCTIONS/CLASSES ##
class TestPortholeViewFunctions(TestCase):
    
    def setUp(self):
        self.new_models = CreateTestModels()
        self.new_models.create_job()
        self.new_models.create_cycle()
        self.member = self.new_models.get_member()
        self.client = self.new_models.get_client()
        self.cycle = self.new_models.get_cycle()
       
    def test_convert_dates(self):
        date = '2018-01-01'

        converted_date = view_func.convert_dates(date)

        self.assertEqual(type(converted_date), str)
        self.assertEqual(converted_date, '1.1.2018')

    def test_get_porthole_context(self):
        context = view_func.get_porthole_context(self.cycle.id)

        self.assertEqual(type(context), dict)
        self.assertEqual(context['member'], self.member)
        self.assertEqual(context['client'], self.client)

    def test_files_do_not_exist(self):
        file = view_func.GetFile(self.cycle)
        quote = file.get_quote()
        po = file.get_po()
        invoice =file.get_invoice()

        self.assertEqual(quote, None)
        self.assertEqual(po, None)
        self.assertEqual(invoice, None)

    def test_files_do_exist(self):
        self.new_models.create_quote()
        self.new_models.create_po()
        self.new_models.create_invoice()

        file = view_func.GetFile(self.cycle)
        
        self.assertTrue(file.get_quote())
        self.assertTrue(file.get_po())
        self.assertTrue(file.get_invoice())

    def test_is_there_a_cycle_status(self):
        status = view_func.CycleStatuses(self.cycle).get_cycle_status()

        self.assertTrue(status)

    def test_set_pending_status_to_false(self):
        new_status = view_func.CycleStatuses(self.cycle)
        status = new_status.set_pending()
        pending_status = new_status.get_cycle_status().pending

        self.assertEqual(pending_status, False)

    def test_set_pending_status_to_true(self):
        self.new_models.create_cycle_status()
        status_obj = self.new_models.get_cycle_status()

        status_obj.approve_quote = True
        status_obj.approve_po = True
        status_obj.approve_invoice = True

        status_obj.save(update_fields = ['approve_quote',
                                        'approve_po',
                                        'approve_invoice'])

        status = self.new_models.get_cycle_status()

        self.assertTrue(status)

    #def test_delete_file(self):
     #   self.new_models.create_quote()
      #  url = 'porthole/member/{0}/{1}/{2}/delete'.format(self.member.username,
       #                                                 self.client.username,
        #                                                self.cycle.id)

       # request = RequestFactory.post(url)
        #request.user = self.member
       # SessionMiddleware.process_request(request)
        #request.session.save()
        
      #  delete_file = view_func.DeleteFile(request, self.cycle.id)
       # deleted_po = delete_file.delete_po()

        #self.assertTrue(deleted_po)


