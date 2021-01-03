from django.urls import *
from .views import *

urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('about/',About.as_view(),name='about'),
]