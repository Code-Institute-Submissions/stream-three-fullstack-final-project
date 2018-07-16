from django.test import TestCase
from cycles.models import Cycles
from accounts.models import AllUser
from django.core.files.uploadedfile import SimpleUploadedFile

class TestCyclePortholeViews(TestCase):
    
    def setUp(self):
        AllUser.objects.create_user(first_name='test1admin',
                                                    last_name='test1',
                                                    username='test1admin',
                                                    email='test1admin1@email.com',
                                                    password='password',
                                                    is_member=True,
                                                    is_client=False
                                                    )
        AllUser.objects.create_user(first_name='test1client',
                                        last_name='test1',
                                        username='test1client',
                                        email='test1client@email.com',
                                        password='password',
                                        is_member=False,
                                        is_client=True
                                        )
        new_cycle = Cycles(job_title='job_title',
                        location='location',
                        description='description',
                        member=AllUser.objects.get(username='test1admin'),
                        client=AllUser.objects.get(username='test1client'))
        new_cycle.save()

        self.username = AllUser.objects.get(username='test1admin').username
        self.cycle_id = Cycles.objects.get(job_title='job_title').id
        self.client_username = AllUser.objects.get(username='test1client').username

    def test_porthole_view_returns_template(self):
        url = '/porthole/member/{0}/{1}/{2}/'.format(self.username,
                                                    self.client_username,
                                                    self.cycle_id)
        request = self.client.get(url)
        
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'porthole.html')

    def test_porthole_upload_quote_redirects(self):
        url = '/porthole/member/{0}/{1}/{2}/quote'.format(self.username,
                                                    self.client_username,
                                                    self.cycle_id)

        request = self.client.post(url)
        self.assertEqual(request.status_code, 302)

    def test_porthole_upload_po_redirects(self):
        url = '/porthole/member/{0}/{1}/{2}/po'.format(self.username,
                                                    self.client_username,
                                                    self.cycle_id)
        request = self.client.post(url)
        self.assertEqual(request.status_code, 302)

    def test_porthole_upload_invoice_redirects(self):
        url = '/porthole/member/{0}/{1}/{2}/invoice'.format(self.username,
                                                    self.client_username,
                                                    self.cycle_id)
        request = self.client.post(url)
        self.assertEqual(request.status_code, 302)