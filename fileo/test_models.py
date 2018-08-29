from django.utils import timezone
from accounts.models import AllUser
from managejobs.models import Jobs
from managecycle.models import Cycles
from manageclient.models import MemberClient
from profiles.models import Profile
from cycleporthole.models import Quotes, PurchaseOrder, Invoices
from cyclestatus.models import CycleStatus


## Class Housing All Model Creation for Re-use in Individual App Tests ##
class CreateTestModels():
    ## Create a Member User and a Client User on Initilise ## 
    def __init__(self):
        self.member = AllUser.objects.create_user(first_name='testadmin',
                                                        last_name='test',
                                                        username='testadmin',
                                                        email='testadmin1@email.com',
                                                        password='password',
                                                        is_member=True,
                                                        is_client=False
                                                        )
        self.client = AllUser.objects.create_user(first_name='testclient',
                                                last_name='test',
                                                username='testclient',
                                                email='testclient@email.com',
                                                password='password',
                                                is_member=False,
                                                is_client=True
                                                )
    ## Return the User Member Object ##
    def get_member(self):
        member = AllUser.objects.get(username='testadmin')
        return member

    ## Returnt the User Client Object ##
    def get_client(self):
        client = AllUser.objects.get(username='testclient')
        return client

    ## Create a Job ##     
    def create_job(self):
        new_job = Jobs(job_title='test job',
                        job_number='1',
                        member=self.member,
                        client=self.client)
        new_job.save()
        return new_job

    ## Return the Saved Job Object ##
    def get_job(self):
        job = Jobs.objects.get(member=self.member)
        return job

    ## Create a Cycle##
    def create_cycle(self):
        new_cycle = Cycles(created=timezone.now(),
                            cycle_title='Test Cycle',
                            description='Test Description',
                            location='London',
                            start_date='2018-01-01',
                            end_date='2018-01-01',
                            cycle_value= ('1.00','GBP'),
                            member=self.member,
                            client=self.client,
                            job=self.get_job())
        new_cycle.save()
        return new_cycle

    ## Return the Saved Cycle Object ##
    def get_cycle(self):
        cycle = Cycles.objects.get(member=self.member)
        return cycle

    ## Create a Profile Object ##
    def create_profile(self):
        new_profile = Profile(company='Test Company',
                                phone='+441784938491',
                                position='Boss',
                                user=self.member,
                                address1='Address1',
                                address2='Address2',
                                city='London',
                                region='Middlesex',
                                post_code='Postcode',
                                country='country')

        new_profile.save()

    ## Return the saved Profile Object ##
    def get_profile(self):
        profile = Profile.objects.get(user=self.member)
        return profile

    ## Create a Member/Client Entry ##
    def create_member_client(self):
        new_member_client = MemberClient(created=timezone.now(),
                                        client = self.client,
                                        member = self.member,
                                        profile = self.get_profile())

        new_member_client.save()

    ## Return the Member/Client Object ##
    def get_member_client(self):
        member_client = MemberClient.objects.get(member=self.member)
        return member_client

    ## Create a Quote Entry ##
    def create_quote(self):
        new_quote = Quotes(client=self.client,
                            member=self.member,
                            cycle=self.get_cycle(),
                            is_quote=True,
                            uploaded_at=timezone.now())
        new_quote.save()

    ## Return the Saved Quote Object ##
    def get_quote(self):
        quote = Quotes.objects.get(member=self.member)
        return quote

    ## Create a PO Entry ##
    def create_po(self):
        new_po = PurchaseOrder(client=self.client,
                            member=self.member,
                            cycle=self.get_cycle(),
                            is_po=True,
                            uploaded_at=timezone.now())
        new_po.save()

    ## Return the Saved PO ##
    def get_po(self):
        po = PurchaseOrder.objects.get(member=self.member)
        return po

    ## Create an Invoice ##
    def create_invoice(self):
        new_invoice = Invoices(client=self.client,
                        member=self.member,
                        cycle=self.get_cycle(),
                        is_invoice=True,
                        uploaded_at=timezone.now())
        new_invoice.save()

    ## Return the Saved Invoice Object ##
    def get_invoice(self):
        invoice = Invoices.objects.get(member=self.member)
        return invoice

    ## Create Cycle Status entry ##
    def create_cycle_status(self):
        
        new_status = CycleStatus(approve_quote = False,
                                contest_quote = False,
                                approve_po = False,
                                contest_po = False,
                                approve_invoice = False,
                                contest_invoice = False,
                                complete = False,
                                pending = False,
                                cancelled = False,
                                cycle = self.get_cycle())
        new_status.save()
        
    ## Return Cycle Status Object ##
    def get_cycle_status(self):
        status = CycleStatus.objects.get(cycle=self.get_cycle())
        return status