from rest_framework.generics import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser

from .models import Solicitacao, DocumentoSolicitacao

from .serializers import SolicitacaoSerializer

class CreateSolicitacao(viewsets.GenericViewSet,
						mixins.ListModelMixin,
						mixins.CreateModelMixin):

	authentication_classes = (TokenAuthentication,)
	permissions_classes = (IsAuthenticated,)
	queryset = Solicitacao.objects.all()
	serializer_class = SolicitacaoSerializer


	def get_queryset(self):
		return self.queryset.filter(user=self.request.user).order_by('-user')


	def perform_create(self, serializer):
		serializer.save(user=self.request.user)



class ManagerSolicitacao(viewsets.ViewSet):
	queryset = Solicitacao.objects.all()
	serializer_class = SolicitacaoSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)