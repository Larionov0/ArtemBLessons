from django.urls import path
from .views import *


urlpatterns = [
    path('test/path/lol/', test_lol),
    path('candidates/', candidates)
]
