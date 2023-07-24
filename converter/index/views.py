from django.shortcuts import render, get_object_or_404, HttpResponse


app_name = 'index'


def index(request):
    return render(request, 'users/profile.html')
