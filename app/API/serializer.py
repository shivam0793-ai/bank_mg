from rest_framework.serializers import ModelSerializer
from app.models import create_account_model


class serializer_view(ModelSerializer):
    class Meta:
        model=create_account_model
        fields='__all__'