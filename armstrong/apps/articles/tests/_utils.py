from django.test import TestCase as DjangoTestCase
from django.utils import unittest
from django.test.client import Client
import fudge
import random
from armstrong.dev.tests.utils import ArmstrongTestCase
from armstrong.hatband.tests._utils import HatbandTestMixin

class ArticlesTestCase(HatbandTestMixin, ArmstrongTestCase):
    pass
