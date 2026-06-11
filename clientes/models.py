from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome completo')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    endereco = models.CharField(max_length=300, verbose_name='Endereço', blank=True)
    cidade = models.CharField(max_length=100, verbose_name='Cidade', blank=True)
    estado = models.CharField(max_length=2, verbose_name='Estado', blank=True)
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome
