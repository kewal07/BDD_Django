from rest_framework import generics

from .models import Transaction
from .serializers import TransactionSerializer, TransactionCreateSerializer


class TransactionView(generics.ListCreateAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	permission_classes = []

	def get_serializer_class(self):
		if self.request.method == 'GET':
			return TransactionSerializer
		return TransactionCreateSerializer
	
	# The next test/feature should be that user sees only their own transactions; this is not yet done
	# def get_queryset(self):
		# return Transaction.objects.filter(user=request.user)
