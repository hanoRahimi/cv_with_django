from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'resume/index.html')

def about_view(request):
    return render(request, 'resume/about.html')

def resume_view(request):
    return render(request, 'resume/resume.html')

def project_view(request):
    return render(request, 'resume/project.html')

def contact_view(request):
    return render(request, 'resume/contact.html')