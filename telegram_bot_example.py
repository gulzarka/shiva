from PHPSupport.telegram_bot.models import (Clarification, Client, Request,
                                            Subcontractor)

# Клиент/подрядчик по telegram id 
Client.objects.get(telegram_id="id")
Subcontractor.objects.get(telegram_id="id")


# Активен ли клиент
Client.objects.get(name='Николай').is_active

# Реквесты клиента
Client.objects.get(name='Николай').requests.all()

# Открытые реквесты
Request.objects.filter(status='open').all()

# Уточнение по реквесту
Request.objects.get(client__name='Николай', status='working').clarifications.all()
