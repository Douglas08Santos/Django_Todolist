Criar um Ambiente Virtual para executar a aplicação

Criar o banco de dados a ser usado 

	- python manage.py migrate

Atualizar o banco com os modelos criados ou atualizados
	- python manage.py makemigrations

Iniciar servidor

	- python manage.py runserver

Criar super usuario para usar a aplicação
	
	-  python manage.py createsuperuser

	- pode ser logar na rota /admin
		+ admin
		+ password

Após criar um novo modelo, adicionar em admin.py:
	- from .models import <nomeModel>
	- admin.site.register(nomeModel)
