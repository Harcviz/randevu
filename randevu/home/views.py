import calendar
from datetime import date

from django.shortcuts import render


def hello_world(request):
    today = date.today()
    month_days = calendar.monthrange(today.year, today.month)[1]

    def day_or_last(day_number: int) -> int:
        return min(day_number, month_days)

    instructors = [
        {"id": "burhan", "name": "Burhan", "badge": "bg-purple-500/20 text-purple-100", "color": "#a855f7"},
        {"id": "selin", "name": "Selin", "badge": "bg-cyan-500/20 text-cyan-100", "color": "#22d3ee"},
        {"id": "emre", "name": "Emre", "badge": "bg-emerald-500/20 text-emerald-100", "color": "#34d399"},
    ]



    sample_bookings = [
        {
            "date": date(today.year, today.month, day_or_last(5)).isoformat(),
            "time": "09:30",
            "instructor": "burhan",
            "title": "İlk görüşme",
            "client": "Ayşe K.",
            "duration": 30,
        },
        {
            "date": date(today.year, today.month, day_or_last(5)).isoformat(),
            "time": "11:00",
            "instructor": "selin",
            "title": "Strateji seansı",
            "client": "Mert D.",
            "duration": 45,
        },
        {
            "date": date(today.year, today.month, day_or_last(12)).isoformat(),
            "time": "14:15",
            "instructor": "emre",
            "title": "Kontrol ve çözüm",
            "client": "Zeynep L.",
            "duration": 30,
        },
        {
            "date": date(today.year, today.month, day_or_last(18)).isoformat(),
            "time": "10:15",
            "instructor": "burhan",
            "title": "Program takibi",
            "client": "Baran S.",
            "duration": 15,
        },
        {
            "date": date(today.year, today.month, day_or_last(25)).isoformat(),
            "time": "16:00",
            "instructor": "selin",
            "title": "Premium danışmanlık",
            "client": "Deniz Y.",
            "duration": 60,
        },
    ]


    highlights = [
        {
            "title": "Akıllı Randevu Akışı",
            "desc": "Günü seç, 15 dk slotları ve hocayı belirle, tek ekranda kaydet.",
        },
        {"title": "Renkli Takip", "desc": "Her hoca için ayrı renk; yoğunluk ve uygunluk anında görünür."},
        {"title": "Günlük Döküm", "desc": "Seçilen günün randevuları otomatik listelenir; filtrele ve paylaş."},
        {"title": "Hızlı Aksiyon", "desc": "Randevu oluşturma, aktarım ve iptal akışları dakikalar sürmez."},
    ]
    return render(
        request,
        "home.html",
        {
            "today": today,
            "instructors": instructors,
            "bookings": sample_bookings,
            "highlights": highlights,
        },
    )
