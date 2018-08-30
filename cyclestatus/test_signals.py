from django.test import TestCase
from django.db import models
from django.dispatch import Signal, receiver
from unittest import mock
from .models import CycleStatus
from .signals import reset_quote_status
from cycleporthole.test_signals import CatchSignal
from accounts.models import AllUser
from fileo.test_models import CreateTestModels

class TestResetStatusOnSignal(TestCase):

    def setUp(self):
        self.new_models = CreateTestModels()
        self.job = self.new_models.create_job()
        self.cycle = self.new_models.create_cycle()
        self.status = self.new_models.get_cycle_status()
        self.new_models.create_quote()
        self.quote = self.new_models.get_quote()
    
    def test_reset_quote_status(self):
        self.status.approve_quote = True
        self.status.contest_quote = True
        self.status.save(update_fields=['approve_quote',
                                    'contest_quote'])

        reset = reset_quote_status(self.quote)

        print(self.status.approve_quote)
        self.assertFalse(reset.approve_quote)
       
       