from django.apps import AppConfig


class AlunoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aluno'

    def ready(self):
        import aluno.signals  # Importa os sinais quando o app for carregado
