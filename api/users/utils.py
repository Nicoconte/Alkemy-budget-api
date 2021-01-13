from rest_framework.authtoken.models import Token

from api.balance.models import Balance

def get_user_from_token(request):
    token_key = request.META.get("HTTP_AUTHORIZATION").replace("Token ", "")
    token = Token.objects.get(key=token_key)
    return token.user


def get_balance_from_user(user):
    return Balance.objects.get(user=user)

