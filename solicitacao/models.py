from django.db import models
from django.conf import settings

class Solicitacao(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='solicitacao', on_delete=models.CASCADE)
	tipoSolicitacao = models.CharField('Tipo de Solicitação', max_length=120)
	data = models.DateTimeField()
	status = models.BooleanField(default=True)
	deferida = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Solicitação'
		verbose_name_plural = 'Solicitações'

	def __str__(self):
		return self.tipoSolicitacao


class DocumentoSolicitacao(models.Model):
	solicitacao = models.ForeignKey(Solicitacao, related_name='documento', on_delete=models.CASCADE)
	upload = models.FileField(upload_to='solicitacao_documentos', max_length=255)
	nome = models.CharField('Nome Documento', max_length=100)
	tipo = models.CharField('Categoria/Tipo', max_length=80)

	class Meta:
		verbose_name = 'Documento Solicitacao'
		verbose_name_plural = 'Documentos Solicitacao'

	def __str__(self):
		return self.filePath