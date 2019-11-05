from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    developed_by = "Jatin"
    employees = [
        "Rishab",
        "Ankit",
        "Yash",
        "Ranpreet",
        "Sheenky",
        "Akshay"
    ]

    context = {
        "developer": developed_by,
        "employees": employees
    }
    response = render(request, 'index.html', context)
    return response