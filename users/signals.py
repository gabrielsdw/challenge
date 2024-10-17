from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_migrate)
def create_default_superuser(sender, **kwargs):
    try:
        User = get_user_model()

        username = 'admin'
        password = '123'
        email = 'admin@gmail.com'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f'Superusuário "{username}" criado com sucesso.')
        else:
            print(f'Superusuário "{username}" já existe.')
    except: 
        pass