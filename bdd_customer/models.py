from django.db import models

TransactionType = (
	("CRE", "Payment credited"),
	("DEB", "Payment made"),
)

CardType = (
	("CRE", "Credit card"),
	("DEB", "Debit card"),
)
class Transaction(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_transaction')
	amount = models.IntegerField()
	type_of_transaction = models.CharField(max_length=3, choices=TransactionType, default= TransactionType[0])


class Card(models.Model):
    name = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    type_of_card = models.CharField(max_length=3, choices=CardType, default= TransactionType[0])
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_card')

    def get_bank(self):
        return self.name + ' belongs to ' + self.bank + ' bank.'

    def __repr__(self):
        return self.name + ' is added.'