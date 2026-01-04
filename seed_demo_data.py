import os
import django
import random
from datetime import date, timedelta, time

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from home.models import Instructor, Appointment, GlobalSettings

def seed_data():
    print("Demo veriler oluşturuluyor...")
    
    # Clear existing data
    Appointment.objects.all().delete()
    Instructor.objects.all().delete()
    GlobalSettings.objects.all().delete()

    # Create Settings
    settings = GlobalSettings.objects.create(
        start_time="08:00",
        end_time="17:00",
        appointment_duration=15
    )

    # Create Instructors
    instructors = [
        Instructor.objects.create(id_name='burhan', name='Burhan', color='#a855f7'),
        Instructor.objects.create(id_name='selin', name='Selin', color='#22d3ee'),
        Instructor.objects.create(id_name='emre', name='Emre', color='#10b981'),
    ]

    today = date.today()
    
    # Create appointments for the next 30 days with varying density
    for i in range(30):
        current_date = today + timedelta(days=i)
        
        # Random density for each day
        # 0: Empty, 1: Low, 2: Medium, 3: High
        density = random.choice([0, 1, 2, 3])
        
        if density == 0: continue
        
        num_appointments = {1: 5, 2: 15, 3: 30}[density]
        
        for _ in range(num_appointments):
            inst = random.choice(instructors)
            
            # Random time between 08:00 and 16:45
            h = random.randint(8, 16)
            m = random.choice([0, 15, 30, 45])
            app_time = time(h, m)
            
            # Check if slot is already taken for this instructor
            if not Appointment.objects.filter(instructor=inst, date=current_date, time=app_time).exists():
                Appointment.objects.create(
                    instructor=inst,
                    date=current_date,
                    time=app_time,
                    title=f"Demo Randevu {random.randint(100, 999)}",
                    client_full_name=f"Müşteri {random.randint(1, 100)}",
                    phone="05000000000",
                    duration=15
                )

    print("Başarıyla tamamlandı! Takvimdeki renk değişimlerini ve barları kontrol edebilirsiniz.")

if __name__ == "__main__":
    seed_data()
