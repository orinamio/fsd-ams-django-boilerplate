from rest_framework import generics
from rest_framework.response import Response

from .models import Account
from .serializers import AccountSerializer


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AccountSerializer(queryset, many=True)
        return Response(dict(data=serializer.data))