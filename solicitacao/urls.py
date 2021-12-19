from django.urls import path

from solicitacao import views

app_name = 'solicitacao'

urlpatterns = [
	path('create/', views.CreateSolicitacao.as_view(), name="create")
]