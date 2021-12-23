from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

from .models import Endereco, Contato, Documento, Ingredient


class ContatoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contato
		fields = (
			'telefone',
			'celular'
		)

	def update(self, instance, validated_data):
		contato = Contato.objects.get(user_id = instance)
		contato.telefone = validated_data['telefone']
		contato.celular = validated_data['celular']
		contato.save()

		return contato


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

	def update(self, instance, validated_data):
		endereco = Endereco.objects.get(user_id = instance)
		endereco.estado = validated_data['estado']
		endereco.cidade = validated_data['cidade']
		endereco.numero = validated_data['numero']
		endereco.rua = validated_data['rua']
		endereco.bairro = validated_data['bairro']
		endereco.complemento = validated_data['complemento']
		endereco.cap = validated_data['cep']
		endereco.save()

		return endereco


class DocumentoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Documento
		fields = (
			'upload',
			'nome',
			'tipo'
		)


class UserSerializer(serializers.ModelSerializer):
	endereco = EnderecoSerializer()
	contato = ContatoSerializer()
	documento = DocumentoSerializer(many=True)

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
			#'foto',
			'endereco',
			'contato',
			'documento',
		)


	def create(self, validated_data):
		endereco_data = validated_data.pop('endereco')
		contato_data = validated_data.pop('contato')

		"""get document uploaded by user"""
		#documentos_data = validated_data.pop('documento')

		user = get_user_model().objects.create_user(**validated_data)

		if user is not None:
			endereco = Endereco.objects.create(user=user, **endereco_data)
			contato = Contato.objects.create(user=user, **contato_data)
			#Documento.objects.create(user=user, **documentos_data)

			for documento_data in documentos_data:
				Documento.objects.create(user=user, **documento_data)

		return user


	def update(self, instance, validated_data):

		ContatoSerializer.update(self, instance, validated_data['contato'])
		EnderecoSerializer.update(self, instance, validated_data['endereco'])
		#DocumentoSerializer

		password = validated_data.pop('password', None)
		contato = validated_data.pop('contato', None)
		endereco = validated_data.pop('endereco', None)

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
	 	#email = attrs.get('email')
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


class IngredientSerializer(serializers.ModelSerializer):

	class Meta:
		model = Ingredient
		fields = ('id,', 'name')
		read_only_fields = ('id')