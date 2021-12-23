from rest_framework import serializers
from .models import Solicitacao, DocumentoSolicitacao
from django.conf import settings



class DocumentoSolicitacaoSerializer(serializers.ModelSerializer):

	class Meta:
		model = DocumentoSolicitacao
		fields = (
			'upload',
			'nome',
			'tipo'
		)



class SolicitacaoSerializer(serializers.ModelSerializer):
	documento = DocumentoSolicitacaoSerializer(many=True)
	#documento = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Solicitacao
		fields = (
			#'user',
			'tipoSolicitacao',
			'data',
			'status',
			'deferida',
			'documento'
		)