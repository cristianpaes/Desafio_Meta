DESAFIO - EMPRESA META

É um desafio criado pela empresa Meta para cadastrar Emissoras e Audiências e exibir as 
informações conforme os critérios informados.

Pré-requisitos
Ter instalado Python3 e pip e instalar o requirements do projeto.


    pip install -r requirements.txt

Apos, rodar os comandos para criar o banco de dados.


    python manage.py makemigrations
    python manage.py migrate

Com o banco de dados criado, se preferir crie o super usuário para administração do django. O mesmo irá pedir nome de usuário, senha e e-mail.


    python manage.py createsuperuser

basta rodar o projeto.


    python manage.py runserver
