from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'resume/index.html')

def about_view(request):
    return render(request, 'resume/about.html')

def resume_view(request):
    return render(request, 'resume/resume.html')

def services_view(request):
    return render(request, 'resume/services.html')

def portfolio_view(request):
    return render(request, 'resume/portfolio.html')

def contact_view(request):
    return render(request, 'resume/contact.html')