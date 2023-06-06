from django.shortcuts import render

# Create your views here.
def coursesview(request):
    return render(request, 'LMS/courses.html')