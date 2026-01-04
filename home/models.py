from django.db import models

class Instructor(models.Model):
    id_name = models.CharField(max_length=50, unique=True) # e.g., 'burhan'
    name = models.CharField(max_length=100)
    badge_class = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=7, default='#22d3ee') # hex color

    def __str__(self):
        return self.name

class GlobalSettings(models.Model):
    start_time = models.TimeField(default="09:00")
    end_time = models.TimeField(default="17:00")

    class Meta:
        verbose_name = "Global Settings"
        verbose_name_plural = "Global Settings"

class Appointment(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    title = models.CharField(max_length=200, default="Yeni randevu")
    client_full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    attendees = models.PositiveIntegerField(default=1)
    duration = models.PositiveIntegerField(default=15) # in minutes
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.date} {self.time} - {self.client_full_name}"
