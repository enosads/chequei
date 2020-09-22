from django.contrib.auth.models import User

from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='usuario')


class Evento(models.Model):
    descricao = models.CharField(max_length=255)
    horario = models.DateField()
    codigo = models.CharField(max_length=6)
    quantidade_de_vagas = models.IntegerField()
    criador = models.ForeignKey('Usuario', on_delete=models.PROTECT, related_name='evento')
    endereco = models.ForeignKey('Endereco', on_delete=models.PROTECT, )


class Endereco(models.Model):
    ACRE = 'Acre'
    AMAPA = 'Amapá'
    ALAGOAS = 'Alagoas'
    AMAZONAS = 'Amazonas'
    BAHIA = 'Bahia'
    CEARA = 'Ceará'
    DISTRITO_FEDERAL = 'Distrito Federal'
    ESPIRITO_SANTO = 'Espírito Santo'
    GOIAS = 'Goiás'
    MARANHAO = 'Maranhão'
    MATO_GROSSO = 'Mato Grosso'
    MATO_GROSSO_DO_SUL = 'Mato Grosso do Sul'
    MINAS_GERAIS = 'Minas Gerais'
    PARA = 'Pará'
    PARAIBA = 'Paraíba'
    PARANA = 'Paraná'
    PERNAMBUCO = 'Pernambuco'
    PIAUI = 'Piauí'
    RIO_DE_JANEIRO = 'Rio de Janeiro'
    RIO_GRANDE_DO_NORTE = 'Rio Grande do Norte'
    RIO_GRANDE_DO_SUL = 'Rio Grande do Sul'
    RONDONIA = 'Rondônia'
    RORAIMA = 'Roraima'
    SANTA_CATARINA = 'Santa Catarina'
    SAO_PAULO = 'São Paulo'
    SERGIPE = 'Sergipe'
    TOCANTINS = 'Tocantins'

    ESTADOS_CHOICES = (
        (ACRE, ACRE),
        (AMAPA, AMAPA),
        (ALAGOAS, ALAGOAS),
        (AMAZONAS, AMAZONAS),
        (BAHIA, BAHIA),
        (CEARA, CEARA),
        (DISTRITO_FEDERAL, DISTRITO_FEDERAL),
        (ESPIRITO_SANTO, ESPIRITO_SANTO),
        (GOIAS, GOIAS),
        (MARANHAO, MARANHAO),
        (MATO_GROSSO, MATO_GROSSO),
        (MATO_GROSSO_DO_SUL, MATO_GROSSO_DO_SUL),
        (MINAS_GERAIS, MINAS_GERAIS),
        (PARA, PARA),
        (PARAIBA, PARAIBA),
        (PARANA, PARANA),
        (PERNAMBUCO, PERNAMBUCO),
        (PIAUI, PIAUI),
        (RIO_DE_JANEIRO, RIO_DE_JANEIRO),
        (RIO_GRANDE_DO_NORTE, RIO_GRANDE_DO_NORTE),
        (RIO_GRANDE_DO_SUL, RIO_GRANDE_DO_SUL),
        (RONDONIA, RONDONIA),
        (SANTA_CATARINA, SANTA_CATARINA),
        (RORAIMA, RORAIMA),
        (SAO_PAULO, SAO_PAULO),
        (SERGIPE, SERGIPE),
        (TOCANTINS, TOCANTINS)
    )

    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255, choices=ESTADOS_CHOICES)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT, )

    def __str__(self):
        return '%s - %s - %s' % (self.rua, self.bairro, self.numero)


class Vaga(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT, )
    evento = models.ForeignKey('Evento', on_delete=models.PROTECT, )
