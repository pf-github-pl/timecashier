from django.urls import path, include
from .views import home, index, about, client_nearby, change_password

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('entry', home, name='entry'),
    path('ajax/client_nearby/', client_nearby, name='client_nearby'),
    path('change_password/', change_password, name='change_password'),
]