from typing import List
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from .models import Film


def Home(request):
    films=list(Film.objects.all().values())
    data={"films":films}

    # films=Film.objects.all()
    return JsonResponse(data)





    