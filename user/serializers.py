from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

from .models import Endereco, Contato, Documento, Solicitacao


class ContatoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contato
		fields = (
			'telefone',
			'celular'
		)


class EnderecoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Endereco
		fields = (
			'estado',
			'cidade',
			'numero',
			'rua',
			'bairro',
			'complemento',
			'cep'
		)


class DocumentosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Documento
		fields = (
			'upload',
			'nome',
			'tipo'
		)



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
		return Solicitacao.objects.create(user=user, **validated_data)




class UserSerializer(serializers.ModelSerializer):
	endereco = EnderecoSerializer()
	contato = ContatoSerializer()
	documento = DocumentosSerializer(many=False)

	class Meta:
		model = get_user_model()
		fields = (
			'email',
			'password',
			'nome',
			'genero',
			'cpf',
			'rg',
			'cnh',
			'pis_pasep',
			'dataNascimento',
			'eleitorNumero',
			'nomeMae',
			'nomePai',
			'naturalidade',
			'cargo',
			'foto',
			'endereco',
			'contato',
			'documento'
		)


	def create(self, validated_data):
		endereco_data = validated_data.pop('endereco')
		contato_data = validated_data.pop('contato')
		documentos_data = validated_data.pop('documento')

		user = get_user_model().objects.create_user(**validated_data)
		Endereco.objects.create(user=user, **endereco_data)
		Contato.objects.create(user=user, **contato_data)

		for documento_data in documentos_data:
			Documento.objects.create(user=user, **documento_data)

		return user


	def update(self, instance, validated_data):
		password = validated_data.pop('password', None)
		user = super().update(instance, validated_data)

		if password:
			user.set_password(password)
			user.save()

		return user



class AuthTokenSerializer(serializers.Serializer):
	cpf = serializers.CharField()
	password = serializers.CharField(
		style = {'input_type': 'password'},
		trim_whitespace = False
	)

	def validate(self, attrs):
	 	email = attrs.get('email')
	 	cpf = attrs.get('cpf')
	 	password = attrs.get('password')

	 	user = authenticate(
	 		request = self.context.get('request'),
	 		username = cpf,
	 		password = password
	 	)

	 	if not user:
	 		msn = 'Unable to authenticate provided'
	 		raise serializers.ValidationError(msn, code = 'athenticate')

	 	attrs['user'] = user
	 	return attrs