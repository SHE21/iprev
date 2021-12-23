from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.parsers import FormParser, MultiPartParser


from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
	""" Criar um novo usuario no sistema"""
	serializer_class = UserSerializer
	#parser_classes = (MultiPartParser, FormParser,)


class CreateTokenView(ObtainAuthToken):
	""" Cria um novo token para o usuário """
	serializer_class = AuthTokenSerializer
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
	serializer_class = UserSerializer
	authentication_classes = (authentication.TokenAuthentication,)
	permissions_classes = (permissions.IsAuthenticated,)


	def get_object(self):
		return self.request.user