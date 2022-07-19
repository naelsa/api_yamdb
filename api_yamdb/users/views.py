from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.generate_code import send_mail_to_user
from users.models import User
from users.permissions import IsAdmin
from users.serializers import (
    UserSerializer, RegistrationSerializer, RegTokSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdmin]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'

    @action(methods=['GET', 'PATCH'], detail=False,
            permission_classes=[IsAuthenticated], url_path='me')
    def user_me(self, request):
        if request.method != 'PATCH':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data.get('role'):
            serializer.validated_data['role'] = request.user.role
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def signup_user(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    user, _ = User.objects.get_or_create(
        username=username,
        email=email
    )
    confirmation_code = default_token_generator
    user.email
    send_mail_to_user(email, confirmation_code)
    return Response(serializer.data,
                    status=status.HTTP_200_OK)


@api_view(['POST'])
def get_token(request):
    serializer = RegTokSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get('username')
    user = get_object_or_404(User, username=username)
    confirmation_code = serializer.data.get('confirmation_code')
    if not default_token_generator.check_token(user, confirmation_code):
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user.is_active = True
    serializer.save()
    token = RefreshToken.for_user(user)
    return Response(
        {'token': str(token.access_token)}, status=status.HTTP_200_OK
    )
