import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from bdd_customer.models import Card
from bdd_customer.serializers import CardSerializer

class TodoListCreateAPIViewTestCase(APITestCase):
    url = reverse("cards")

    def setUp(self):
        self.username = "johndoe"
        self.password = "password"
        self.email = "email_john@doe.com"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_card(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.post(self.url, {"name": "GoldPlus", "bank": "AMEX"})
        self.assertEqual(201, response.status_code)

    def test_user_cards(self):
        self.client.login(username='johndoe', password='password')
        card = Card.objects.create(user=self.user, name="New Amex", bank="AMEX")
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Card.objects.count())