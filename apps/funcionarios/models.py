from django.db import models
# on_delete=models.PROTECT ( serve para quando o user for deletado ele deletar na class Funcionario )
from django.contrib.auth.models import User
#user pode estar em multiplos departamentos
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa



class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
