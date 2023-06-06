from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'LMS/index.html')

def aboutview(request):
    return render(request, 'LMS/about.html')

def testimonialview(request):
    return render(request, 'LMS/testimonial.html')

def teamview(request):
    return render(request, 'LMS/team.html')

def contactview(request):
    return render(request, 'LMS/contact.html')
