from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/path/lol/', test_lol),
    path('candidates/', candidates)
]
