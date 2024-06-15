from django.urls import path
from .views import index, response

urlpatterns = [
    path('', index, name='index'), #This assigns a name to the URL pattern which can be used to refer to it in templates and other parts of your code.
    path('response', response, name='response')
]
