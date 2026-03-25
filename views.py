from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})


class TransferViewset(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    def create(self, request):
        sender_id = request.data.get('sender')
        receiver_id = request.data.get('receiver')
        amount = float(request.data.get('amount'))

        try:
            sender = User.objects.get(id=sender_id)
            receiver = User.objects.get(id=receiver_id)

        except User.DoesNotExist:
            return Response({'error': 'Sender or Receiver does not exists!'}, status=status.HTTP_404_NOT_FOUND)

        if sender.id == receiver.id:
            return Response({'error': 'Cannot make transfer to the same account!'}, status=status.HTTP_400_BAD_REQUEST)

        if sender.balance < amount:
            return Response({'error': 'Insuffiecient balance!'}, status=status.HTTP_400_BAD_REQUEST)

        sender.balance -= amount
        receiver.balance += amount

        sender.save()
        receiver.save()

        transactions = Transfer.objects.create(
            sender=sender, receiver=receiver, amount=amount, sender_balance=sender.balance, receiver_balance=receiver.balance)
        serializer = TransferSerializer(transactions)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


def transaction_list(request):
    transactions = Transfer.objects.all()
    return render(request, 'history.html', {'transactions': transactions})
