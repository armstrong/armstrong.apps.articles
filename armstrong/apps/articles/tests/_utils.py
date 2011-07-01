from django.test import TestCase as DjangoTestCase
from django.utils import unittest
from django.test.client import Client
import fudge
import random
from armstrong.hatband.tests._utils import HatbandTestMixin, patch_settings

class ArticlesTestCase(HatbandTestMixin, DjangoTestCase):
    
    def setUp(self):
        fudge.clear_expectations()
        fudge.clear_calls()
        
