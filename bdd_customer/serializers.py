from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Transaction, Card


class TransactionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Transaction
		fields = ('id', 'amount', 'type_of_transaction')

class TransactionCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Transaction
		fields = ('user', 'amount', 'type_of_transaction')

class CardSerializer(serializers.ModelSerializer):
	
	user = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = Card
		fields = '__all__'
