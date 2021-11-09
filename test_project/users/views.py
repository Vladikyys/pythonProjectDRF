from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .license import IsOwnerProfileOrReadOnly
from .models import CustomUser
from .renderers import UserJSONRenderer
from .serializers import RegistrationSerializer


# class RegistrationAPIView(APIView):
#     """
#     Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
#     """
#     permission_classes = (AllowAny,)
#     serializer_class = RegistrationSerializer
#     renderer_classes = (UserJSONRenderer,)
#
#     def post(self, request):
#         user = request.data.get('user', {})
#         # Паттерн создания сериализатора, валидации и сохранения - довольно
#         # стандартный, и его можно часто увидеть в реальных проектах.
#         serializer = self.serializer_class(data=user)
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
class UserListCreateView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny,]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny,]
