from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from rest_framework.authtoken.models import Token
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    EmailField
)
from .models import (
    AreaAplicacao,
    Licenca,
    TipoObra,
    TipoPerfil,
    Commentary,
    CommentaryReply,
    Obra,
    Perfil
)
from .related_fields import (
    UserComentarioRelatedFields,
    UserLoginRelatedFields
)

# Global Variables for setting password
hasher = PBKDF2PasswordHasher()

class AreaAplicacaoSerializer (ModelSerializer):
    class Meta:
        model = AreaAplicacao
        fields = (
            'name',
            'state',
            'data_creation'
        )
        extra_kwargs = {'data_creation': {'read_only': True}}

class TipoObraSerializer (ModelSerializer):
    class Meta:
        model = TipoObra
        fields = (
            'name',
            'description',
            'state',
            'data_creation'
        )
        extra_kwargs = {'data_creation': {'read_only': True}}

class LicencaSerializer (ModelSerializer):
    class Meta:
        model = Licenca
        fields = (
            'name',
            'description',
            'state',
            'data_creation'
        )
        extra_kwargs = {'data_creation': {'read_only': True}}

class TipoPerfilSerializer (ModelSerializer):
    class Meta:
        model = TipoPerfil
        fields = (
            'name',
            'state',
            'date_creation'
        )
        extra_kwargs = {'date_creation': {'read_only': True}}

class CommentarySerializer (ModelSerializer):
    class Meta:
        model = Commentary
        fields = (
            'commentary',
            'obra',
            'user',
            'data_commentary',
            'state'
        )
        extra_kwargs = {
            'state': {'read_only': True},
            'data_commentary': {'read_only': True}}

class CommentaryReplySerializer (ModelSerializer):
    class Meta:
        model = CommentaryReply
        fields = (
            'reply',
            'commentary',
            'user',
            'data_reply',
            'state'
        )
        extra_kwargs = {
            'data_reply': {'read_only': True},
        }

class ObraSerializer (ModelSerializer):
    class Meta:
        model = Obra
        fields = (
            'name',
            'description',
            'type_obra',
            'licenca',
            'data_creation',
            'url'
        )
        extra_kwargs = {
            'data_registered': {'read_only': True}
        }

class UserCreateAccountSerialiazer (ModelSerializer):
    token = CharField(allow_blank=True, read_only=True) 
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'date_joined',
            'is_active',
            'last_login',
            'token'
        )
        extra_kwargs = {
            'date_joined': {'read_only': True},
            'is_active': {'read_only': True},
            'last_login': {'read_only': True},
            'password': {'write_only': True}
        }
    
    def create (self, validate_data):
        username = validate_data['username']
        email = validate_data['email']
        first_name = validate_data['first_name']
        last_name = validate_data['last_name']
        password = validate_data['password']
        
        hashed_password = hasher.encode(password, salt='salt', iterations=100000)

        user = User.objects.create(password=hashed_password, username=username, first_name=first_name,
        last_name=last_name,email=email, is_active=False)

        token = Token.objects.create(user=user)
        return user

class UserLoginSerializer (ModelSerializer):
    user = UserLoginRelatedFields(read_only=True)
    username = CharField()
    email = EmailField()
    password = CharField()

    class Meta:
        model = Perfil
        fields = (
            'user',
            'picture',
            'state',
            'area',
            'profile_type',
            'username',
            'email',
            'password'
        )
        extra_kwargs = {
            'picture' : {'read_only': True},
            'state' : {'read_only': True},
            'area' : {'read_only': True},
            'profile_type' : {'read_only': True}
        }
    
    def validate (data):
        return data