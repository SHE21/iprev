from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Solicitacao

from .serializers import SolicitacaoSerializer

class CreateSolicitacao(generics.CreateAPIView):
	serializer_class = SolicitacaoSerializer
	authentication_classes = (TokenAuthentication,)
	permissions_classes = (IsAuthenticated,)

	def get_object(self):
		print(self.request.user.email)
		return self.request.user

	"""def create(self, validated_data):
		solicitacao = Solicitacao.objects.create(user=self.request.user, **validated_data)
		return solicitacao"""