from django.test import TestCase
from fileo.test_models import CreateTestModels



class TestCyclePortholeModels(TestCase):
    
    def setUp(self):
        new_models = CreateTestModels()
        new_models.create_job()
        new_models.create_cycle()
        new_models.create_quote()
        new_models.create_po()
        new_models.create_invoice()

        self.member = new_models.get_member()
        self.client = new_models.get_client()
        self.cycle = new_models.get_cycle()
        self.quote = new_models.get_quote()
        self.po = new_models.get_po()
        self.invoice = new_models.get_invoice()
       

    def test_quotes_model(self):
        quote = self.quote

        self.assertEqual(self.member.username, quote.member.username)
        self.assertEqual(self.client.username, quote.client.username)
        self.assertEqual(self.cycle.cycle_title, quote.cycle.cycle_title)
        self.assertTrue(quote.is_quote)

    def test_po_model(self):
        po = self.po

        self.assertEqual(self.member.username, po.member.username)
        self.assertEqual(self.client.username, po.client.username)
        self.assertEqual(self.cycle.cycle_title, po.cycle.cycle_title)
        self.assertTrue(po.is_po)

    def test_invoice_model(self):
        invoice = self.invoice

        self.assertEqual(self.member.username, invoice.member.username)
        self.assertEqual(self.client.username, invoice.client.username)
        self.assertEqual(self.cycle.cycle_title, invoice.cycle.cycle_title)
        self.assertTrue(invoice.is_invoice)
            
