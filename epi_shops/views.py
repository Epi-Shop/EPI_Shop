from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'epi_shops/global/homepage.html')

def login(request):
    return render(request, 'epi_shops/global/login.html')

def create_user(request):
    return render(request, 'epi_shops/global/create_user.html')

def shop(request):
    return render(request, 'epi_shops/global/shop.html')

def admin(request):
    return render(request, 'epi_shops/global/admin.html')
