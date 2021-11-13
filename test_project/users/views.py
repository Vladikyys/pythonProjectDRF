from django.http import Http404, HttpResponse
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .license import IsOwnerProfileOrReadOnly
from .models import CustomUser, Announcement
from .renderers import UserJSONRenderer
from .serializers import RegistrationSerializer, AnnouncementSerializer


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
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny, ]


class AnnouncementView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = RegistrationSerializer

    def get(self, request):
        announcement = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcement, many=True)
        return Response({"announcement": serializer.data})

    def post(self, request):
        announcement = request.data
        owner_id = request.data['owner']
        owner = CustomUser.objects.get(pk=owner_id)
        if owner.status == 'Customer':
            serializer = AnnouncementSerializer(data=announcement)
            if serializer.is_valid(raise_exception=True):
                announcement_saved = serializer.save()
        else:
            return Response({'User': 'This user is not a Customer'}, status=404)
        return Response({"success": f"Announcement '{announcement_saved.title}' created successfully"})


class AnnouncementExecutorView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        announcement_id = request.data['announcement_id']
        announcement = Announcement.objects.get(pk=announcement_id)
        executor_id = request.data['executor_id']
        executor = CustomUser.objects.get(pk=executor_id)
        if announcement is None:
            return Response({'Error': 'This announcement is not created'}, status=404)
        if executor.status != "Executor":
            return Response({'Error': 'This user is not executor'}, status=404)
        announcement.status = 'Executing'
        announcement.executor = executor
        announcement.save()
        return Response({"success": "The executor started to perform the announcement"})



