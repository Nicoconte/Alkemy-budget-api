from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.authtoken.models import Token

from api.balance.models import Balance

import json

class UserRegister(APIView):
    #Register
    def post(self, request):
        try:
            body = json.loads(request.body)
            print(body)

            user = User.objects.create_user(username=body['username'], email=body['email'], password=body['password'])

            if user:
                Balance.objects.create(user=user)
                token = Token.objects.create(user=user)

                return Response({
                    "username" : user.username,
                    "key" : token.key
                }, status=status.HTTP_200_OK)
            
            else:
                raise Exception

        except Exception as e:
            return Response({
                "details" : str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class UserAuth(APIView):
    def post(self, request):
        try:
            body = json.loads(request.body)
            print(body)

            user = authenticate(request, username=body['username'], password=body['password'])

            if user:
                token = Token.objects.get(user=user)

                return Response({   
                    "username" : user.username,
                    "key" : token.key
                }, status=status.HTTP_200_OK)
            
            else:
                return Response({
                    "details" : "Invalid credentials"
                }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                "details" : str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

