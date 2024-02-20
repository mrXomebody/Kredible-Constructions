# main/views.py

from django.shortcuts import render
from .models import Service, PortfolioItem

def home(request):
    return render(request, 'main/home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services})

def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'main/portfolio.html', {'portfolio_items': portfolio_items})

# Add similar views for other sections (contact, about, etc.)
