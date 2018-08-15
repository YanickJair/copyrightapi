from django.contrib.auth.models import User
from rest_framework.serializers import RelatedField
from .models import (
    Obra
)

class UserComentarioRelatedFields (RelatedField):
    def to_representation (self, value):
        return {
            'id': value.id,
            'first_name': value.first_name,
            'last_name': value.last_name
        }

class UserLoginRelatedFields (RelatedField):
    def to_representation (self, value):
        return {
            'id': value.id,
            'username': value.username,
            'email': value.email, 
            'password': value.password,
            'first_name': value.first_name,
            'last_name': value.last_name,
            'is_active': value.is_active,
            'last_login': value.last_login,
            'date_joined': value.date_joined
        }
class ObraRelatedFields (RelatedField):
    pass