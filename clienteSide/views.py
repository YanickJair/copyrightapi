from django.contrib.auth.models import User
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import (
    TipoObra,
    AreaAplicacao,
    Licenca,
    TipoPerfil,
    Commentary,
    CommentaryReply,
    Obra
)
from .serializers import (
    AreaAplicacaoSerializer,
    TipoObraSerializer,
    LicencaSerializer,
    TipoPerfilSerializer,
    CommentarySerializer,
    CommentaryReplySerializer,
    ObraSerializer,
    UserCreateAccountSerialiazer
)

# Create your views here.
class AreaAplicacaoList (ListCreateAPIView):
    queryset = AreaAplicacao.objects.all()
    serializer_class = AreaAplicacaoSerializer

class AreaAplicacaoDetail (RetrieveUpdateDestroyAPIView):
    queryset = AreaAplicacao.objects.all()
    serializer_class = AreaAplicacaoSerializer

class TipoObraList (ListCreateAPIView):
    queryset = TipoObra.objects.all()
    serializer_class = TipoObraSerializer

class TipoObraDetail (RetrieveUpdateDestroyAPIView):
    queryset = TipoObra.objects.all()
    serializer_class = TipoObraSerializer

class LicencaList (ListCreateAPIView):
    queryset = Licenca.objects.all()
    serializer_class = LicencaSerializer

class LicencaDetail (RetrieveUpdateDestroyAPIView):
    queryset = Licenca.objects.all()
    serializer_class = LicencaSerializer

class TipoPerfilList (ListCreateAPIView):
    queryset = TipoPerfil.objects.all()
    serializer_class = TipoPerfilSerializer

class TipoPerfilDetail (RetrieveUpdateDestroyAPIView):
    queryset = TipoPerfil.objects.all()
    serializer_class = TipoPerfilSerializer

class CommentaryList (ListCreateAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer

class CommentaryDetail (RetrieveUpdateDestroyAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer

class CommentaryReplyList (ListCreateAPIView):
    queryset = CommentaryReply.objects.all()
    serializer_class = CommentaryReplySerializer

class CommentaryReplyDetail (RetrieveUpdateDestroyAPIView):
    queryset = CommentaryReply.objects.all()
    serializer_class = CommentaryReplySerializer

class ObraList (ListCreateAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

class ObraDetail (RetrieveUpdateDestroyAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

class UserList (ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateAccountSerialiazer

class UserDetail (RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateAccountSerialiazer