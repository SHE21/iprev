from django.urls import path, include
from rest_framework.routers import DefaultRouter

from solicitacao import views


router = DefaultRouter()
router.register('create', views.CreateSolicitacao)
router.register('update', views.ManagerSolicitacao)


app_name = 'solicitacao'

urlpatterns = [
	path('', include(router.urls)),
]