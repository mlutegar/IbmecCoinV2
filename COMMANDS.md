# GIT

Comando para atualizar o repositório:

```bash
$ git pull
```

Comando para adicionar todos os arquivos:

```bash
$ git add .
```

Comando para fazer commit dos arquivos:

```bash
$ git commit -m "feat: adicionando grupos" --no-verify
```

Comando para fazer push dos arquivos:

```bash
$ git push --no-verify
```

# DJANGO 

Para atualizar o banco de dados, execute os comandos abaixo:

```bash
$ python manage.py makemigrations
```

```bash
$ python manage.py migrate
```

Para rodar o servidor, execute o comando abaixo:

```bash
$ python manage.py runserver
```

Para rodar o servidor em uma porta específica, execute o comando abaixo:

```bash
python manage.py runserver 0.0.0.0:8000
```

Para criar um super usuário, execute o comando abaixo:

```bash
$ python manage.py createsuperuser
```

Criar um app no Django, execute o comando abaixo:

```bash
$ python manage.py startapp aluno
```