from django.db import models

TransactionType = (
	("CRE", "Payment credited"),
	("DEB", "Payment made"),
)

class Transaction(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_transaction')
	amount = models.IntegerField()
	type_of_transaction = models.CharField(max_length=3, choices=TransactionType, default= TransactionType[0])

