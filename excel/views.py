from django.shortcuts import render
from datetime import datetime, timedelta

def hello(request):
  return render(request, 'hello.html', {})


def dashboard(request):
    context = {
        'total_cases': 223456789,
        'total_deaths': 4567890,
        'total_recovered': 201234567,
        'active_cases': 17654332,
    }

    context['countries'] = [
        {'name': 'USA', 'total_cases': 45678901, 'total_deaths': 789012, 'total_recovered': 40123456},
        {'name': 'India', 'total_cases': 34567890, 'total_deaths': 456789, 'total_recovered': 31234567},
        {'name': 'Brazil', 'total_cases': 23456789, 'total_deaths': 345678, 'total_recovered': 20123456},
        {'name': 'France', 'total_cases': 12345678, 'total_deaths': 234567, 'total_recovered': 10987654},
        {'name': 'UK', 'total_cases': 9876543, 'total_deaths': 123456, 'total_recovered': 8765432},
    ]

    today = datetime.now()
    context['chart_data'] = {
        'labels': [(today - timedelta(days=i)).strftime('%d-%m-%Y') for i in range(30, 0, -1)],
        'datasets': [{
            'label': 'Nuevos casos diarios',
            'data': [
                154321, 162345, 158765, 149876, 163456, 157890, 151234,
                168765, 172345, 169876, 165432, 173456, 177890, 174321,
                181234, 179876, 183456, 187890, 184321, 188765, 192345,
                189876, 195432, 193456, 197890, 201234, 198765, 203456,
                207890, 204321
            ],
        }]
    }

    return render(request, 'dashboard.html', context)

def upload(request):
  return render(request, "upload.html", {})

def edit(request):
  return render(request, "edit.html", {})

def create(request):
  return render(request, "create.html", {})