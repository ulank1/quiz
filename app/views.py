from datetime import datetime
from random import randrange

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet, FCMDeviceViewSet
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from app.models import *
from app.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('-name')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['id', 'login']
    search_fields = ['name']


class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Test.objects.all().order_by('-name')
    serializer_class = TestSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['name', 'id', 'category', 'lang']


class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'test']


class RatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Rating.objects.order_by('-created_at')
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'user', 'created_at']


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'name', 'lang']


class GameQuizGameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GameQuizGame.objects.all()
    serializer_class = GameQuizGameSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'user_owner', 'user_outer', 'outer_point']


class MainCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MainCategory.objects.order_by('id')
    serializer_class = MainCategorySerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'lang']


class DayQuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DayQuiz.objects.all()
    serializer_class = DayQuizSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'date', 'lang']


class InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'main_category', 'lang']


class UniversityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'lang']


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.order_by('main_category')
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'main_category', 'lang']


def game_quiz_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        test = request.GET.get("test")
        # snippets = [user for user in User.objects.all() if user.phone == 'qweqwrqwe']
        snippets = GameQuiz.objects.filter(test=test)
        true_snippets = []

        for x in range(0, 3):
            true_snippets.append(snippets[randrange(len(snippets))])

        serializer = GameQuizSerializer(true_snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


def game_quiz_list_outer(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        test = request.GET.get("testtr")
        tests = test.split(',')

        # snippets = [user for user in User.objects.all() if user.phone == 'qweqwrqwe']

        true_snippets = []

        for x in range(0, 3):
            true_snippets.append(GameQuiz.objects.get(pk=int(tests[x])))

        serializer = GameQuizSerializer(true_snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


class CountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = QuizCount.objects.all()
    serializer_class = CountSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'date']


class UniversitySubCategoryViewSet(viewsets.ModelViewSet):
    queryset = UniversitySubCategory.objects.all()
    serializer_class = UniversitySubCategorySerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'university']


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.order_by('created_at')
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'name', 'lang']


class OrtViewSet(viewsets.ModelViewSet):
    queryset = ORT.objects.all()
    serializer_class = OrtSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'name', 'lang']


class OrtDescViewSet(viewsets.ModelViewSet):
    queryset = ORTDesc.objects.all()
    serializer_class = OrtDescSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'ort']


class RatingAll(APIView):

    def get(self, request):
        if request.method == 'GET':

            user_id = request.GET.get('user_id')

            rating = Rating.objects.order_by('-rating')
            rating = rating.filter(created_at='all')
            my_rating = rating.filter(user=user_id)

            if len(rating) <= 0:
                serializer = RatingSerializer(rating, many=True)
                return Response({'size': len(rating), 'data': RatingSerializer(my_rating, many=True).data})
            else:
                my_id = my_rating[0].user_id
                _size = len(rating)

                first_rating = []

                if _size > 2:
                    first_rating = [rating[0], rating[1], rating[2]]
                elif _size == 2:
                    first_rating = [rating[0], rating[1]]
                elif _size == 1:
                    first_rating = [rating[0]]

                position = 0
                for i in range(_size):
                    if my_id == rating[i].user_id:
                        position = i + 1

                return Response({'size': position, 'first': RatingAllSerializer(first_rating, many=True).data,
                                 'rating': RatingAllSerializer(rating, many=True).data})


class GameInviteAll(APIView):

    def get(self, request):
        if request.method == 'GET':
            user_id = request.GET.get('user_id')

            true_game = []

            game = GameQuizGame.objects.order_by('-id')

            owner = game.filter(user_owner=user_id)
            for onw in owner:
                true_game.append(onw)

            outer = game.filter(user_outer=user_id)

            for out in outer:
                true_game.append(out)

            return JsonResponse(GameQuizGameSerializerGandon(game, many=True).data, safe=False)


class GameAll(APIView):

    def get(self, request):
        if request.method == 'GET':
            quiz = str(request.GET.get('quiz'))

            true_game = []
            game = GameQuiz.objects.all()

            quizzes = quiz.split(',')

            for q in quizzes:
                ga = game.filter(pk=int(q))
                true_game.append(ga[0])

            return JsonResponse(GameQuizSerializer(true_game, many=True).data, safe=False)


class FCMDeviceCreateView(FCMDeviceViewSet):
    serializer_class = FCMDeviceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'success': True}, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NotificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['user']

    def get_queryset(self):
        notification = self.queryset
        for notif in notification:
            if not notif.is_view:
                notif.is_view = True
                notif.save()

        return notification


class NotificationCount(APIView):

    def get(self, request):
        if request.method == 'GET':
            user = request.GET.get('user')
            notifs = Notification.objects.filter(user=user)

            s = 0

            for notif in notifs:
                if not notif.is_view:
                    s = s + 1

            return Response({"size": s})
