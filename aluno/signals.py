from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Grupo


@receiver(m2m_changed, sender=Grupo.alunos.through)
def verificar_limite_alunos(sender, instance, action, **kwargs):
    """Impede que um grupo tenha mais alunos do que o limite definido."""
    if action in ["post_add", "post_remove", "post_clear"]:
        if instance.alunos.count() > instance.limite_aluno:
            raise ValidationError(f"O grupo '{instance.nome}' não pode ter mais de {instance.limite_aluno} alunos.")
