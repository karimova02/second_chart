
from django.urls import path
from .views import * 
urlpatterns = [
    path('', home),
    path('bar/', bar), 
    path('line/', line),
    path('pie/', pie),
    path('flow/', flow),
    path('gantt/', gantt),
    path('solid/', solid)
    ]