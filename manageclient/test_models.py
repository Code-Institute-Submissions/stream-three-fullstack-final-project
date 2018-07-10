from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import MemberClient
from accounts.models import AllUser

class TestMemberClient(TestCase):
    def test_create_an_entry(self):
        member = 'admin'
        client = 'client'
        AllUser.objects.create_user(first_name='test',
                                        last_name='test',
                                        username=member,
                                        email='testmember@email.com',
                                        password='password',
                                        is_member=True,
                                        is_client=False
                                        )
        AllUser.objects.create_user(first_name='test',
                                        last_name='test',
                                        username=client,
                                        email='testclient@email.com',
                                        password='password',
                                        is_member=True,
                                        is_client=False
                                        )
        
        member = get_object_or_404(AllUser, username=member)
        client = get_object_or_404(AllUser, username=client)
        entry = MemberClient(member=member, client=client)
        entry.save()

        self.assertEqual(member, entry.member)
        self.assertEqual(client, entry.client)