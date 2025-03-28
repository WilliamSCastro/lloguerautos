from django.core.management.base import BaseCommand
import random
from faker import Faker
from django.contrib.auth.models import User
from lloguer.models import *
from datetime import timedelta

faker = Faker()

class Command(BaseCommand):

    def handle(self, *args, **options):

        cotxes = []
        for i in range(4):
            marca = faker.company()
            model = faker.word().capitalize()
            matricula = faker.license_plate()
            cotxe = Automobil(marca=marca, model=model, matricula=matricula)
            cotxe.save()
            print(f"Created: {cotxe}")
            cotxes.append(cotxe)
        
        for i in range(8):
            username = faker.unique.user_name()
            email = faker.email()
            password = 'testpass123'  # Contrasenya comuna per a prova
            user = User.objects.create_user(username=username, email=email, password=password)

            num_reserves = random.randint(1, 2)
            for j in range(num_reserves):
                cotxe = random.choice(cotxes)
                data_inici = faker.date_between(start_date='-30d', end_date='+30d')
                # Assegurar que data_final és posterior a data_inici
                data_final = data_inici + timedelta(days=random.randint(1, 14))
                if not Reserva.objects.filter(cotxe=cotxe, data_inici=data_inici).exists():
                    reserva = Reserva(user=user,cotxe=cotxe,data_inici=data_inici,data_final=data_final)
                    reserva.save()
                    print(f"Created reserva: {reserva}")

        


    
