from __future__ import unicode_literals
from django.db import models


class Projeto(models.Model):
    nome = models.CharField(verbose_name=u"Nome Projeto", max_length=100)
    link = models.CharField(verbose_name=u"Link", max_length=100)
    dataInicio = models.DateField(verbose_name=u"Data Inicio",  auto_now_add=False)
    dataFim = models.DateField(verbose_name=u"Data Fim",  auto_now_add=False)
    descricao = models.TextField(verbose_name=u"Descrição", null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Projetos"


class Conhecimento(models.Model):
    nome = models.CharField(verbose_name=u"Nome Conhecimento", max_length=100)
    nivel = models.PositiveIntegerField(verbose_name=u"Nivel Conhecimento", default=0)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Conhecimentos"


class DadosPessoal(models.Model):
    imagen = models.ImageField(verbose_name=u"Imagem Perfil", upload_to='pic_folder/')
    nome = models.CharField(verbose_name=u"Nome ", max_length=100)
    idade = models.PositiveIntegerField(verbose_name=u"Idade")
    email = models.EmailField(verbose_name=u"E-mail")
    github = models.CharField(verbose_name=u"github", max_length=100, null=True, blank=True)
    linkdin = models.CharField(verbose_name=u"linkdin", max_length=100, null=True, blank=True)
    ddd = models.CharField(verbose_name=u"DDD", max_length=3)
    celuar = models.CharField(verbose_name=u"celeular", max_length=9)
    descricao = models.TextField(verbose_name=u"Descrição", null=True, blank=True)
    conhecimento = models.ManyToManyField(Conhecimento, related_name="conhecimento", verbose_name=u"Conhecomento")
    projetos = models.ManyToManyField(Projeto, related_name="projetos", verbose_name=u"Projetos")
    dataNacimento = models.DateField(verbose_name=u'Data Nascimento', auto_now=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "DadosPessoais"
