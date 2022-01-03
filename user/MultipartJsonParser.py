from django.http import QueryDict
import json
from rest_framework import parsers


class MultipartJsonParser(parsers.MultiPartParser):

	def parse(self, stream, media_type=None, parser_context=None):
		result = super().parse(
			stream,
			media_type=media_type,
			parser_context=parser_context
		)

		data = {}
		data = json.loads(result.data['data'])
		qdic = QueryDict('', mutable=True)
		qdic.update(data)

		return parsers.DataAndFiles(qdic, result.files)