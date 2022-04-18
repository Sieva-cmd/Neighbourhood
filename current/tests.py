from django.test import TestCase

from django.test import TestCase
from .models import Post, NeighbourHood,Business,Profile
from django.contrib.auth.models import User
import datetime as dt



# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.karen = NeighbourHood(name='Karen',location ='Nairobi',hood_logo ='images/nairobi_west.jpg',description ='A home away from home',health_tell='0729485780',police_number='07293057894',area_administrator='Benjamin Nzulu')

    def test_instance(self):
        self.assertTrue(isinstance(self.karen,NeighbourHood))

    def tearDown(self):
        NeighbourHood.objects.all().delete()

    def test_save_method(self):
        self.karen.create_neighborhood()
        hood = NeighbourHood.objects.all()
        self.assertTrue(len(hood)>0)

    # def test_delete_method(self):
    #     self.karen.create_neighborhood('karen')
    #     test_neighborhood =NeighbourHood(name='Karen',location ='Nairobi',hood_logo ='images/nairobi_west.jpg',description ='A home away from home',health_tell='0729485780',police_number='07293057894',area_administrator='Benjamin Nzulu')
    #     test_neighborhood.create_neighborhood()
    #     self.karen.delete_neighborhood()
    #     self.assertTrue(len(NeighbourHood)<1)

class PostTestClass(TestCase):
    def setUp(self):
        self.new_post = Post(title='Test',post='test data',date='18/04/2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def tearDown(self):
        Post.objects.all().delete()

    # def test_save_method(self):
    #     self.new_post.save_post()
    #     rest = Post.objects.all()
    #     self.assertTrue(len(rest)>0)

    # def test_delete_method(self):
    #     self.new_post.delete_post('new_post')
    #     rest = Post.objects.all()
    #     self.assertTrue(len(rest)==0)