from django.test import TestCase
from managecycle.models import Cycles
from accounts.models import AllUser
from django.core.files.uploadedfile import SimpleUploadedFile
from .view_func import get_porthole_context
from managejobs.models import Jobs

class TestCyclePortholeViews(TestCase):
    ## Build Model Objects ##
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
        
        new_job = Jobs(job_title='testjob',
                        job_number='1',
                        location='testlocation',
                        start_date='now',
                        end_date='tomorrow',
                        member=AllUser.objects.get(username='test1admin'),
                        client=AllUser.objects.get(username='test1client'),
                        )
        new_job.save()
        new_cycle = Cycles(cycle_title='cycle_title',
                        description='description',
                        member=AllUser.objects.get(username='test1admin'),
                        client=AllUser.objects.get(username='test1client'),
                        job=Jobs.objects.get(job_title='testjob'))
        new_cycle.save()

        self.username = 'test1admin'
        self.cycle_id = Cycles.objects.get(cycle_title='cycle_title').id
        self.client_username = 'test1client'

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

    def test_get_porthole_info_is_correct(self):
        username = 'test1admin'
        cycle_id = self.cycle_id
        client_username = 'test1client'
        porthole_info = get_porthole_info(username, cycle_id, client_username)

        self.assertEqual(type(porthole_info), dict)
        self.assertEqual(porthole_info['cycle'].id, cycle_id)
        self.assertEqual(porthole_info['member'].username, username)
        self.assertEqual(porthole_info['client'].username, client_username)