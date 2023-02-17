from .models import Subcontractor, Client


def is_user_suncontractor(user_id):
    return Subcontractor.objects.filter(telegram_id=user_id).first()


def is_user_client(user_id):
    return Client.objects.filter(telegram_id=user_id).first()
