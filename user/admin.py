from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user import models

class UserAdmin(BaseUserAdmin):
	ordering = ['id']
	list_display = ['nome', 'cpf', 'email']

	fieldsets = (
		(None, {'fields': ('email', 'password')}),

		('Informações Pessoais',
			{'fields':
				(
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
					'foto'
				)
			}
		),

		('Permissões',
			{'fields':
				(
					'is_active',
					'is_staff',
					'is_superuser',
					'groups',
					'user_permissions'
				)
			}
		),

		('Datas', {'fields': ('last_login', 'date_joined')}),
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2')
		}),
	)


admin.site.register(models.User, UserAdmin)
