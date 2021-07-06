from django.urls import path
from api import viewsets

urlpatterns=[
    path('company/',viewsets.company_api),
    path('review/',viewsets.review_api),
]