from django.test import TestCase
from django.test import Client


class UserTest(TestCase):

    def loginTest(self):
		self.credentials = {
            'username': 'admin',
            'password': 'Fd9Km_'}
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
		
	def loginFailTest(self):
		self.credentials = {
            'username': 'admin00',
            'password': 'admin123'}
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)