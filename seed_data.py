import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from home.models import Instructor

def seed():
    instructors = [
        {"id_name": "burhan", "name": "Burhan", "badge_class": "bg-purple-500/20 text-purple-100", "color": "#a855f7"},
        {"id_name": "selin", "name": "Selin", "badge_class": "bg-cyan-500/20 text-cyan-100", "color": "#22d3ee"},
        {"id_name": "emre", "name": "Emre", "badge_class": "bg-emerald-500/20 text-emerald-100", "color": "#34d399"},
    ]

    for inst in instructors:
        Instructor.objects.get_or_create(
            id_name=inst["id_name"],
            defaults={
                "name": inst["name"],
                "badge_class": inst["badge_class"],
                "color": inst["color"]
            }
        )
    print("Seed data created successfully.")

if __name__ == "__main__":
    seed()
