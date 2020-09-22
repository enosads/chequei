from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from mobile import serializers


class LoginAPI(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, ):
        serializer = serializers.LoginMembroSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user=user)
                membro = user.membro
                data = {}
                data.update(serializers.UsuarioSerializer(instance=membro, context={'request': request}).data),
                response = Response(data, status=status.HTTP_200_OK)
            elif User.objects.filter(username=username).count() > 0:

                data = {"error": 'Senha inválida'}
                response = Response(data, status=status.HTTP_401_UNAUTHORIZED)
            else:
                data = {
                    "error": 'Nome de usuário inválido'}
                response = Response(data, status=status.HTTP_401_UNAUTHORIZED)
        else:
            data = {
                "error": 'Não foi possível fazer login'}
            response = Response(data, status=status.HTTP_404_NOT_FOUND)

        return response


class LoginPorTokenAPI(APIView):

    def get(self, request, ):

        user = request.user
        if user:
            membro = user.membro
            data = {}
            data.update(serializers.UsuarioSerializer(instance=membro, context={'request': request}).data),
            response = Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "error": 'Não foi possível fazer login'}
            response = Response(data, status=status.HTTP_404_NOT_FOUND)

        return response
