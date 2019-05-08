from django.test import TestCase
from bdd_customer.models import Card
from django.contrib.auth.models import User

class CardTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="john_doe_card", password="password")
        Card.objects.create(name="Platinum", bank="HDFC", type_of_card="CRE", user=user)
        Card.objects.create(name="Gold", bank="ICICI", type_of_card="DEB", user=user)

    def test_card_bank(self):
        card_hdfc = Card.objects.get(name='Platinum')
        card_icici = Card.objects.get(name='Gold')
        self.assertEqual(card_hdfc.get_bank(), "Platinum belongs to HDFC bank.")
        self.assertEqual(card_icici.get_bank(), "Gold belongs to ICICI bank.")