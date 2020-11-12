from django.contrib.auth import get_user_model
from django.db import models
from ordered_model.models import OrderedModel


class Turma(OrderedModel):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    matriculas = models.ManyToManyField(get_user_model())
