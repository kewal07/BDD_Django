from rest_framework import generics

from .models import Transaction, Card
from .serializers import TransactionSerializer, TransactionCreateSerializer, CardSerializer

class TransactionListCreateAPIView(generics.ListCreateAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	permission_classes = []

	def get_serializer_class(self):
		if self.request.method == 'GET':
			return TransactionSerializer
		return TransactionCreateSerializer
	
	# The next test/feature should be that user sees only their own transactions; this is not yet done ; done for TDD, see cards view below
	# def get_queryset(self):
		# return Transaction.objects.filter(user=self.request.user)



class CardListCreateAPIView(generics.ListCreateAPIView):
	serializer_class = CardSerializer

	def get_queryset(self):
		return Card.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
