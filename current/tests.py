from django.test import TestCase

from django.test import TestCase
from .models import Post, NeighbourHood
from django.contrib.auth.models import User
import datetime as dt



# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Mlolongo = NeighbourHood(neighbourhood='Gashville')

    def test_instance(self):
        self.assertTrue(isinstance(self.Mlolongo,NeighbourHood))

    def tearDown(self):
        NeighbourHood.objects.all().delete()

    def test_save_method(self):
        self.Mlolongo.create_neighborhood()
        hood = NeighbourHood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Mlolongo.delete_neighborhood('Kahawa')
        hood = NeighbourHood.objects.all()
        self.assertTrue(len(hood)==0)

class PostTestClass(TestCase):
    def setUp(self):
        self.Munch = Post(munch='Munch')

    def test_instance(self):
        self.assertTrue(isinstance(self.Munch))

    def tearDown(self):
        Post.objects.all().delete()

    def test_save_method(self):
        self.Munch.save_post()
        rest = Post.objects.all()
        self.assertTrue(len(rest)>0)

    def test_delete_method(self):
        self.Munch.delete_post('Munch')
        rest = Post.objects.all()
        self.assertTrue(len(rest)==0)