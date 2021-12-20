from rest_framework.generics import mixins
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
	media_type = 'application/x-www-form-urlencoded'
	#parser_classes = [FileUploadParser]


	def get_queryset(self):
		return self.queryset.filter(user=self.request.user).order_by('-user')


	def perform_create(self, serializer):
		documento = self.request.documento
		#print(documento.nome)
		##DocumentoSolicitacao.objects.create(solicitacao=,**documento)
		serializer.save(user=self.request.user)

	"""def create(self, validated_data):
		solicitacao = Solicitacao.objects.create(user=self.request.user, **validated_data)
		return solicitacao"""