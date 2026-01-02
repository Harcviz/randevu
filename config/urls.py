from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('api/appointments/', views.get_appointments, name='get_appointments'),
    path('api/appointments/save/', views.save_appointment, name='save_appointment'),
    path('api/appointments/delete/<int:app_id>/', views.delete_appointment, name='delete_appointment'),
]
