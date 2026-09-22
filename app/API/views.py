from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from app.models import create_account_model
from .serializer import serializer_view

class api_view(ModelViewSet):
    queryset=create_account_model.objects.all()
    serializer_class=serializer_view
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]