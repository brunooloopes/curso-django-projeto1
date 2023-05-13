from django.http import HttpResponse
from django.urls import path
from recipes.views import home, contato, sobre


def my_view(request):
    return HttpResponse('Uma linda string')
    # return HTTP Response


urlpatterns = [
    path('', my_view),
    path('home/', home),
    path('contato/', contato),
    path('sobre/', sobre)
]
