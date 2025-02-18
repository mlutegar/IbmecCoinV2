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


@receiver(m2m_changed, sender=Grupo.alunos.through)
def validar_aluno_na_turma(sender, instance, action, pk_set, **kwargs):
    """
    Impede que alunos que não estão na turma do grupo sejam adicionados.
    """
    if action == "pre_add":
        for aluno_id in pk_set:
            if not instance.turma.alunos.filter(pk=aluno_id).exists():
                raise ValidationError(f"O aluno de ID {aluno_id} não pertence à turma '{instance.turma}'.")