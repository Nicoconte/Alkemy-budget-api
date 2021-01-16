from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.authentication import TokenAuthentication


from .models import Operation
from .serializers import OperationSerializer


from api.balance.utils import update_balance_money, update_balance_after_delete, get_balance_money
from api.users.utils import get_balance_from_user, get_user_from_token

from datetime import datetime

import json

# Create your views here.
class OperationsView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            body = json.loads(request.body)
            date = datetime.today().strftime('%Y-%m-%d')
            user = get_user_from_token(request)

            if body['money'] > get_balance_money(user) and body['type'] == "egreso":
                return Response({
                    "details" : "No tenes saldo suficiente para el onlyfans de sasha grey"
                }, status=status.HTTP_400_BAD_REQUEST)

            op = Operation.objects.create(user=user, concept=body['concept'], money_amount=body['money'], date=date, type=body['type'])
            
            if op:
                update_balance_money(user, body['money'], body['type'])

                return Response({
                    "success" : True
                }, status=status.HTTP_200_OK)


        except Exception as e:
            return Response({
                "details" : str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            body = json.loads(request.body)
            user = get_user_from_token(request)

            op = Operation.objects.get(id=id, user=user)

            if op:
                op_actual_money = op.money_amount


                if body['money'] < op_actual_money and op.type == "ingreso":
                    return Response({
                        "details" : "No se puede modificar el dinero ingresado. Cancele la operacion"
                    }, status=status.HTTP_400_BAD_REQUEST)

                op.concept = body['concept']
                op.money_amount = body['money']
                op.save()

                update_balance_money(user, (body['money'] - op_actual_money), op.type)

                return Response({
                    "success" : True
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "details" : str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user = get_user_from_token(request)
            
            op = Operation.objects.get(id=id, user=user)

            if op:
                update_balance_after_delete(user, op.money_amount, op.type) #Actualizamos el balance 
                op.delete() #Eliminamos la operacion

                return Response({
                    "success" : True
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "details" : str(e)
            }, status=status.HTTP_400_BAD_REQUEST) 

    def get(self, request, id):
        try:
            user = get_user_from_token(request)
            op = Operation.objects.get(id=id, user=user)

            if op:
                serializer = OperationSerializer(op)

                return Response(serializer.data)

        except Exception as e:
            return Response({
                "details" : str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class ListOperations(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = get_user_from_token(request)
            op = Operation.objects.filter(user=user)

            if op and len(op) > 0:
                serializer = OperationSerializer(op, many=True)

                return Response(serializer.data)

        except Exception as e:
            return Response({
                "details" : str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class ListLatestOperations(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = get_user_from_token(request)
            op = Operation.objects.filter(user=user).order_by('-pk')
            serializer = None

            if len(op) >= 10:
                serializer = OperationSerializer(op[0:10], many=True)

            else:                
                serializer = OperationSerializer(op, many=True)
            
            return Response(serializer.data)

        except Exception as e:
            return Response({
                "details" : str(e)
            }, status=status.HTTP_400_BAD_REQUEST)    