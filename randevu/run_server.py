import os
from django.core.management import execute_from_command_line


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


if __name__ == "__main__":
    # Run the Django dev server packaged into the executable (no autoreload inside the bundle)
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000", "--noreload"])
