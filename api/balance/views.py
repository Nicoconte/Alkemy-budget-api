from api.balance.serializers import BalanceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.authentication import TokenAuthentication

from .models import Balance

from api.users.utils import get_user_from_token


import json

# Create your views here.

class BalanceView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = get_user_from_token(request)
            balance = Balance.objects.get(user=user)

            if balance:
                serializer = BalanceSerializer(balance)

                return Response(serializer.data, safe=False)
            
        except Exception as e:
            return Response({
                "details" : str(e)
            }, status=status.HTTP_400_BAD_REQUEST)