import json
from datetime import date, datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Instructor, Appointment, GlobalSettings

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def index(request):
    instructors = list(Instructor.objects.values('id_name', 'name', 'badge_class', 'color'))
    settings = GlobalSettings.objects.first()
    if not settings:
        settings = GlobalSettings.objects.create(start_time="09:00", end_time="17:00")
    
    start_time = settings.start_time
    end_time = settings.end_time
    
    if not isinstance(start_time, str):
        start_time = start_time.strftime("%H:%M")
    if not isinstance(end_time, str):
        end_time = end_time.strftime("%H:%M")

    return render(request, "home.html", {
        "instructors": instructors,
        "settings": {
            "start_time": start_time,
            "end_time": end_time,
        }
    })

@csrf_exempt
@login_required
def save_settings(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            settings = GlobalSettings.objects.first()
            if not settings:
                settings = GlobalSettings()
            
            settings.start_time = data.get('start_time', '09:00')
            settings.end_time = data.get('end_time', '17:00')
            settings.save()

            # Update instructors
            instructor_data = data.get('instructors', [])
            for inst in instructor_data:
                Instructor.objects.update_or_create(
                    id_name=inst['id_name'],
                    defaults={
                        'name': inst['name'],
                        'color': inst['color']
                    }
                )
            
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)

@login_required
def get_appointments(request):
    appointments = Appointment.objects.all()
    data = []
    for app in appointments:
        data.append({
            "id": app.id,
            "date": app.date.isoformat(),
            "time": app.time.strftime("%H:%M"),
            "instructor": app.instructor.id_name,
            "title": app.title,
            "client": app.client_full_name,
            "phone": app.phone,
            "attendees": app.attendees,
            "duration": app.duration,
            "note": app.note,
        })
    return JsonResponse(data, safe=False)

@csrf_exempt
@login_required
def save_appointment(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            instructor = Instructor.objects.get(id_name=data['instructor'])
            
            # Parse date and time
            app_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
            app_time = datetime.strptime(data['time'], '%H:%M').time()
            
            app_id = data.get('id')
            if app_id and not str(app_id).startswith('bk-'): # Existing appointment
                appointment = Appointment.objects.get(id=app_id)
            else:
                appointment = Appointment(instructor=instructor)

            appointment.instructor = instructor
            appointment.date = app_date
            appointment.time = app_time
            appointment.title = data.get('title', 'Yeni randevu')
            appointment.client_full_name = data.get('client', '')
            appointment.phone = data.get('phone', '')
            appointment.attendees = int(data.get('attendees', 1))
            appointment.duration = int(data.get('duration', 15))
            appointment.note = data.get('note', '')
            
            appointment.save()
            
            return JsonResponse({"status": "success", "id": appointment.id})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)

@csrf_exempt
@login_required
def delete_appointment(request, app_id):
    if request.method == "DELETE":
        try:
            Appointment.objects.filter(id=app_id).delete()
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)
