from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def test_lol(request):
    return HttpResponse('<h1>LOL page</h1><p>This is my first test page</p>')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/path/lol/', test_lol)
]
