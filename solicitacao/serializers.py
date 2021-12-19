from rest_framework import serializers
from .models import Solicitacao
from django.conf import settings

class SolicitacaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Solicitacao
		fields = (
			'tipoSolicitacao',
			'data',
			'status',
			'deferida'
		)


	def create(self, validated_data):
		return Solicitacao.objects.create(user=self.get_object(), **validated_data)