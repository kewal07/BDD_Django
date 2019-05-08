from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'type_of_transaction')

class TransactionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('user', 'amount', 'type_of_transaction')