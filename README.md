# django-rest-pecas
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/LombaAnderson/django-rest-pecas/blob/main/LICENSE)

# Sobre o projeto
Django-rest-pecas é uma API de cadastro de venda de droids onde é possível ter acesso aos lendários droids de Star Wars e feito no Django admin o acesso possui algumas restrições feitas pelo administrador, exemplificando: o anunciante pode por seus dados na plataforma, porém não pode alterar determinados dados do cadastro como por quem é feito o anúncio. Foi usado o Postman para testar o funcionamento da API e foi feito teste com o próprio Python. Pretendo alterar algumas coisas do projeto posteriormente que faltaram ,pois utilizei uma máquina reserva antiga para terminá-lo devido a placa mãe do computador principal estar no conserto

## Imagem da página API Django
<div align="center">
<img src="https://user-images.githubusercontent.com/60937513/147471361-0a93e086-19d8-46df-a7ab-86003324b786.png" width="600" />
</div>

## Print da verificação feita no Postman
<div align="center">
<img src="https://user-images.githubusercontent.com/60937513/147471546-332911cd-84e2-4a9c-b35f-009e4ada5baf.png" width="800" />
</div>


# Tecnologias utilizadas

- Python
- API Django Rest
- Docker
- asgiref==3.4.1
-black==21.12b0
-click==8.0.3
-colorama==0.4.4
-Django==4.0
-djangorestframework==3.13.1
-mypy-extensions==0.4.3
-pathspec==0.9.0
-Pillow==8.4.0
-platformdirs==2.4.1
-pytz==2021.3
-sqlparse==0.4.2
-tomli==1.2.3
-typing_extensions==4.0.1
-tzdata==2021.5

# Testes unitários e manual
- Python
- Postman

# Instruções para compilar, testar e rodar o projeto

```bash
# Clonar repositório
git clone https://github.com/LombaAnderson/django-rest-pecas

# Criação e acesso da pasta do projeto
-mkdir admin
-cd django-rest-pecas

# Criação do ambiente de desenvolvimento do Python
-python -m venv venv

# Ativar o ambiente de desenvolvimento(venv)
-source venv/Scripts/activate

# Instalação do Django (Atenção: instalar somente após a ativação da venv)
-pip install django

# Instalação do pacote do Django Rest Framework
-pip install django djangorestframework
 
# Comando de criação do projeto
-django-admin startproject core .

# Criação do servidor
-python manage.py runserver

# Instalação do pytz(timezone)
pip install pytz

# Acesso ao servidor Django
http://127.0.0.1:8000/

# Apps 
-django-admin startapp core

# Preparação das migrations
- python manage.py makemigrations

# Envio das migrations configuradas para o banco de dados
- python manage.py migrate

```

# Autor

Anderson Lomba de Oliveira

Linkedin

https://www.linkedin.com/in/anderson-lomba-140279142/

Portfólio

https://www.lombanderson.epizy.com

# Agradecimentos

Agradeço ao meu Deus que é meu tudo e a minha esposa, minha companheira que amo muito!
