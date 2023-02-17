from .models import Subcontractor, Client


def is_user_subcontractor(user_id):
    return Subcontractor.objects.filter(telegram_id=user_id).first()


def is_user_client(user_id):
    return Client.objects.filter(telegram_id=user_id).first()


def add_executer(user_id):
    print('Здесь код добавления')
    new_executer = Subcontractor(telegram_id=user_id, name='Пока одинаковое')
    new_executer.save()

