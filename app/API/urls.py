from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import api_view

rounter=DefaultRouter()
rounter.register('api-view',api_view,basename='api-view')



urlpatterns=[
    path('',include(rounter.urls))
]