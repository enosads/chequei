from rest_framework import serializers
from rest_framework.authtoken.models import Token

from mobile.models import Endereco, Usuario


class LoginMembroSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)
    endereco_id = serializers.PrimaryKeyRelatedField(queryset=Endereco.objects.all(), write_only=True,
                                                     source='endereco', )

    token = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)

    def get_username(self, instance):
        return instance.user.username

    def get_token(self, instance):
        token, created = Token.objects.get_or_create(user=instance.user)
        return token.key

    class Meta:
        model = Usuario
        fields = (
            'id', 'nome', 'telefone', 'email', 'data_nascimento', 'cpf', 'username', 'token',
            'endereco_id', 'imagem')
