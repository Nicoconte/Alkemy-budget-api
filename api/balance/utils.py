from .models import Balance

def update_balance_money(user, money_amount, type):
    balance = Balance.objects.get(user=user)

    if type == "ingreso":
        balance.total_money = balance.total_money + money_amount
    
    elif type == "egreso":
        balance.total_money = balance.total_money - money_amount 
    
    else:
        print("No se esta actualizando")

    balance.save()


def update_balance_after_delete(user, money_amount, type):
    balance = Balance.objects.get(user=user)

    if type == "ingreso":
        balance.total_money = balance.total_money - money_amount
    
    elif type == "egreso":
        balance.total_money = balance.total_money + money_amount 
    
    balance.save()    


def get_balance_money(user):
    balance = Balance.objects.get(user=user)
    return balance.total_money